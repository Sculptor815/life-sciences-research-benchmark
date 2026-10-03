import asyncio
import importlib.metadata


class RunError(Exception):
    def __init__(self, status, retryable=False):
        self.status, self.retryable = status, retryable
        super().__init__(status)


class MockAdapter:
    """Deliberately weak responses; never reads answer keys."""
    version = "builtin-1"

    def __init__(self, config):
        self.model = config["model"]
        self.events = list(config.get("mock_events", []))

    def generate(self, request, config):
        event = self.events.pop(0) if self.events else "ok"
        if event in ("rate_limit", "timeout", "network_error"):
            raise RunError(event, True)
        if event in ("context_limit", "unsupported_image", "api_error"):
            raise RunError(event)
        answer = {"empty": "", "refusal": "I cannot answer this question.", "malformed": "{not-json"}.get(event)
        if answer is None:
            answer = '{"answer":"A","reason":"Mock response for software testing."}' if '"answer"' in request["text"] else "The evidence is insufficient. Check independent biological replicates and alternative explanations."
        return {"text": answer, "model": self.model, "input_tokens": 0, "output_tokens": 0, "provider_cost_usd": 0.0, "stop_reason": "stop"}


class InspectAdapter:
    """Inspect supplies provider clients; Benchmark owns retry and budget records."""
    def __init__(self, config):
        from inspect_ai.model import GenerateConfig, get_model
        self.version = importlib.metadata.version("inspect_ai")
        settings = dict(config.get("generation", {}))
        settings.update(max_tokens=config["max_output_tokens"], max_retries=0, timeout=config["timeout_seconds"])
        self.generation = GenerateConfig(**settings)
        self.model = get_model(config["model"], config=self.generation, memoize=False)
        self.loop = asyncio.Runner()

    def generate(self, request, config):
        from inspect_ai.model import ChatMessageSystem, ChatMessageUser
        from inspect_ai.model import ContentImage, ContentText
        generation = self.generation
        if "seed" in config.get("generation", {}):
            generation = generation.model_copy(update={"seed":config["generation"]["seed"]})
        async def call():
            content = [ContentText(text=request["text"])]
            content.extend(ContentImage(image=url) for url in request["images"])
            output = await self.model.generate(
                [ChatMessageSystem(content=request["system"]), ChatMessageUser(content=content)],
                tools=[], tool_choice="none", config=generation, cache=False,
            )
            if any(getattr(getattr(choice, "message", None), "tool_calls", None) for choice in output.choices):
                raise RunError("forbidden_tool_request")
            usage = output.usage
            return {"text": output.completion, "model": output.model,
                    "input_tokens": usage.input_tokens if usage else None,
                    "output_tokens": usage.output_tokens if usage else None,
                    "provider_cost_usd": None,
                    "stop_reason": str(output.choices[0].stop_reason) if output.choices else "unknown"}
        try:
            return self.loop.run(call())
        except RunError:
            raise
        except Exception as exc:
            status = getattr(exc, "status_code", None)
            name = type(exc).__name__.lower()
            if status == 429:
                raise RunError("rate_limit", True) from None
            if isinstance(exc, (TimeoutError, ConnectionError)) or "timeout" in name or "connection" in name:
                raise RunError("timeout" if "timeout" in name else "network_error", True) from None
            if status and status >= 500:
                raise RunError("network_error", True) from None
            # Avoid storing raw provider exceptions: they may include credentials or packets.
            raise RunError("api_error") from None

    def close(self):
        try:
            self.loop.run(self.model.__aexit__(None, None, None))
        finally:
            self.loop.close()
