# 安装与第一次评测

这个项目的用途是“用同一套题评价不同模型”。现在还提供从原始发现出发的候选题审阅页面，详情见[发现过程与人工审阅](DISCOVERY.zh-CN.md)。已有的七项分析流程检查使用合成数据，属于出题方验证，不是对模型编程能力的评分。

## 1. 放好项目和私有资料

当前 D 盘目录结构如下：

```text
D:\life sciences research workbench\
  life-sciences-research-workbench\  # 可公开的代码与公开题
  life-sciences-research-workbench-private\  # 不上传 GitHub
    draft-keys.json                  # 草稿答案和评分细则
    heldout\                        # 以后编写的保留题
    runs\                           # 模型回答
    reviews\                        # 专家评分和身份对应
    reports\                        # 发布前的报告
```

如果先在其他目录暂存，保持公开项目与私有资料分开：公开目录名为 `life-sciences-research-workbench`，私有目录可命名为 `life-sciences-research-workbench-private`。配置已更新为当前 D 盘运行路径；不要把私有目录拖进 GitHub 上传区。

## 2. 创建 Python 环境

当前 D 盘副本已建立 `.venv` 并完成本地可编辑安装，可以直接使用下文的 `.venv\Scripts\lsrw.exe`。此环境使用现有 Python 3.12.9 的系统包；Inspect AI 和 Streamlit 已安装并通过集成测试。下方命令适用于以后重新创建独立环境。Windows CLI 会自动开启 UTF-8，直接运行测试时请使用 `python -X utf8`。

打开 PowerShell，进入 D 盘的项目文件夹。下面假设你已经安装 Python，并且 `python --version` 显示 3.11 或更新版本。

```powershell
Set-Location 'D:\life sciences research workbench\life-sciences-research-workbench'
$env:PIP_CACHE_DIR = 'D:\life sciences research workbench\pip-cache'
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e .
```

这一步只装本项目，足够运行免费模拟评测。以后需要连接真实模型和打开评分界面时再安装：

```powershell
.\.venv\Scripts\python.exe -m pip install -e '.[runtime,review]'
```

不必修改系统执行策略，也不必激活环境；直接使用 `.venv\Scripts` 里的程序即可。macOS/Linux 将该路径换成 `.venv/bin`，同时修改配置中的输出目录。

## 3. 检查题库

```powershell
.\.venv\Scripts\lsrw.exe validate
```

当前应看到 20 道题且 `valid: true`。这只说明文件结构、标签、图像哈希等检查通过，不代表题目科学性已经获得专家认可。

```powershell
.\.venv\Scripts\lsrw.exe validate --formal
```

这条检查当前会失败：320 题还未建齐，20 道样板也处于草稿状态。这是预期的保护措施。

## 4. 跑一次免费模拟

先打开 `configs/mock.json`，确认 `output_root` 指向你能写入的 D 盘目录。预演不会发送模型请求或生成运行结果。

```powershell
.\.venv\Scripts\lsrw.exe run --config configs/mock.json --dry-run
.\.venv\Scripts\lsrw.exe run --config configs/mock.json
```

记录最后显示的完整运行路径。模拟接口是本地测试程序，不是实际大模型，其分数不能用来评价某家模型。

## 5. 看第一次报告

将以下 `RUN_DIRECTORY` 换成刚才的完整路径，把 `KEY_FILE` 换成私有目录中的草稿答案路径。

```powershell
.\.venv\Scripts\lsrw.exe score --run 'RUN_DIRECTORY' --keys 'KEY_FILE'
.\.venv\Scripts\lsrw.exe report --run 'RUN_DIRECTORY' --output 'D:\life sciences research workbench\life-sciences-research-workbench-private\reports\preview-1'
```

用浏览器打开生成的 `REPORT.html`。同时提供 `report.json` 和 `scores.csv`。开放题显示待评分，总分保留为空；不会把尚未评分的题算成零分。

生成的文件按版本保留。若你再次评分得到另一个版本，生成报告时需要用 `--scores '完整评分文件路径'` 指定版本，并给报告一个新的输出文件夹。

## 6. 两位专家独立评分

```powershell
.\.venv\Scripts\lsrw.exe review --prepare --run 'RUN_DIRECTORY' --keys 'KEY_FILE' --output 'D:\life sciences research workbench\life-sciences-research-workbench-private\reviews\round-1' --reviewers expert-a expert-b
.\.venv\Scripts\lsrw.exe review --queue 'D:\life sciences research workbench\life-sciences-research-workbench-private\reviews\round-1\rater-1\queue.json'
```

评分界面仅在本机 `127.0.0.1` 启动。第二位专家使用 `rater-2` 的队列。每个维度先选择 0–4 分，再写评分依据。分数没有预设默认值；提交后保留原记录。

```powershell
.\.venv\Scripts\lsrw.exe score --run 'RUN_DIRECTORY' --keys 'KEY_FILE' --reviews 'D:\life sciences research workbench\life-sciences-research-workbench-private\reviews\round-1'
```

如果需要裁定，报告会显示 `needs_adjudication`。第三位专家的操作见[出题与评分说明](AUTHORING.zh-CN.md)。

## 7. 连接真实模型前需要填写什么

复制 `configs/api.template.json` 到私有目录，填写：

| 参数 | 你需要决定的内容 |
|---|---|
| `model` | Inspect 支持的供应商/精确模型标识；记录版本，避免只记产品名称 |
| `dataset`、`output_root` | 题库和结果的绝对路径 |
| `track` | `text`、`image` 或 `all`；比较时使用同一批题 |
| `supports_images` | 模型是否确实支持图像；不能用图像答案的文字描述代替 |
| `generation` | 供应商支持的采样或推理参数；不确定的参数先不设置 |
| `max_output_tokens` | 单题输出上限，要与题目字数和模型的推理计费方式相容 |
| `input_token_ceiling` | 输入 token 预留上限，包含图像和消息开销 |
| `budget_usd` | 本轮最多允许预留的预算 |
| 两个 `*_usd_per_million` | 当前输入、输出每百万 token 的美元价格 |
| `pricing_date`、`pricing_source` | 价格核对日期与来源 |

API 密钥由供应商对应的环境变量提供，不写进配置或题目。尚未通过 Workbench 执行付费模型评测；DeepSeek Harness 已使用现有登录账户参与出题和核查，两者分别记录。

先运行 `--dry-run`，核对初次请求数、最多重试次数和估算金额，再运行不带 `--dry-run` 的命令。费用估算依赖你填入的价格和上限，同时在供应商侧配置额度限制。不同厂商的推理预算不被视为完全等价。

`formal` 目前保持 `false`。只有完整题库、专家审核、校准和锁定都完成后才能进行正式保留集评测。

## 下一步先做什么

先阅读 `data/public/items.jsonl` 中的四道生物信息学文本题和私有细则，确认难度与研究场景符合预期。随后邀请各学科的两名审核者和一名裁定人，用这些草稿检验评分是否清楚。等细则稳定，再按覆盖清单扩充题库；这样可以避免在大量题目写完后重新设计评分规则。
