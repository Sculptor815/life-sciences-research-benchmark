# 出题、审核与评分

## 组织方式

四个主学科是分子生物学、生物化学、神经科学、生物信息学。分子实验和生化实验是跨疾病领域的方法基础；癌症、炎症、代谢病等放在研究场景标签中。每道题只能计入一个主学科和一种能力，其余联系放在辅助标签，避免重复计分。

生物信息学题应围绕研究判断出题：数据是否适合使用某种工具，分析单位和统计假设是否正确，结果支持哪一级结论，以及需要什么独立验证。仅背出软件名称不能获得开放题高分。未来若测“真实工具操作”，应另设具有执行环境与数据材料的赛道。

每个学科安排至少两位审核者、一位独立裁定人。名册使用代号，真实身份映射放在私有目录。软件能检查代号是否独立，不能验证专家资历或替代实际审核。

## 先检查现有样板

公开文件 `data/public/items.jsonl` 每行一道题。私有的 `draft-keys.json` 按题号保存答案、证据位置、五维评分细则、各档示例和替代答案。当前 20 题均为 AI 辅助起草，尚无人类专家签字。

每条评分细则目前提供 0–4 档锚点和错误说明。专家需要特别检查相邻档是否足够明确、合理的替代方法是否被接纳，以及错误是否被重复扣分。不要在校准前把这些草稿当作已验证量表。

## 扩充题目

使用 `templates/item.json` 起草题面；答案及开放题细则使用 `templates/open-key.json`，保存到私有目录。参考答案不进入题面 JSONL。`data/coverage-plan.csv` 是 320 个待分配位置的清单，不代表已经完成 320 道题。

每题填写：

1. 唯一题号、案例家族、来源论文家族、版本。
2. 主学科、能力、具体主题、技术、研究场景、难度。
3. 英文题目、固定材料、回答格式与字数限制。
4. 图像题的原始图、处理记录、许可、署名与 SHA-256。
5. 独立答案文件中的依据、证据位置、评分点、部分得分、替代解和关键错误。

图像题必须让图像信息参与作答；不能把答案性文字描述作为文本替代输入。合成图像要明确标为教学/模拟材料，不能冒充实测结果。不同论文或实验案例的相似改写仍属于同一个家族。

论文辨析题要准备足够的固定材料，使模型可以区分来源身份与结论支持程度。出处不确定时允许“材料不足以核实”；已知虚构必须有明确证据或受控合成身份。真实撤稿、更正材料要保存记录日期，避免将过时快照当作实时状态。

## 审核和锁定

每题两位审核者分别完成来源检查、独立试答、细则检查和材料许可检查。私有审核文件格式如下；每个题号均需两条独立记录：

```json
{
  "domain_roster": {
    "molecular_biology": {"reviewers": ["mol-a", "mol-b"], "adjudicator": "mol-c"},
    "biochemistry": {"reviewers": ["bio-a", "bio-b"], "adjudicator": "bio-c"},
    "neuroscience": {"reviewers": ["neu-a", "neu-b"], "adjudicator": "neu-c"},
    "bioinformatics": {"reviewers": ["inf-a", "inf-b"], "adjudicator": "inf-c"}
  },
  "items": {
    "EXAMPLE-ID": [
      {"reviewer": "mol-a", "date": "YYYY-MM-DD", "source_checked": true, "independent_trial_answer": true, "rubric_checked": true, "material_rights_checked": true},
      {"reviewer": "mol-b", "date": "YYYY-MM-DD", "source_checked": true, "independent_trial_answer": true, "rubric_checked": true, "material_rights_checked": true}
    ]
  }
}
```

这只是格式示例，不能作为已完成审批记录。完成实际审核后才将对应题目的 `status` 改成 `reviewed`。

用全部 64 道公开题和预制回答训练评分者。开放题保留双人评分记录；客观题也需完成答案与单位检查。在私有校准文件中保存 `completed_public_ids`、`records`（每项包含 `item_id`、`ability`、`ratings`）、`accepted_by`、`acceptance_rationale` 和 `unresolved_systematic_disagreement: false`。只有实际消除系统性分歧后，才能填写最后一项。

```console
lsrw calibrate --records PRIVATE/pairs.json --output PRIVATE/calibration-summary.json
lsrw lock --dataset PRIVATE/full-bank/items.jsonl --keys PRIVATE/keys.json --approvals PRIVATE/approvals.json --calibration PRIVATE/calibration.json --output PRIVATE/bank-lock.json
```

完整题库必须有 320 题、正确的 16 单元分配，公开与保留家族不能重叠。锁定后，不可修改题目或细则而继续沿用同一评测版本。修改后应重新审核、建立新版本；已经得到的模型回答不能挑选性重跑。

## 实际评分与裁定

每位评分者只拿自己的队列。界面不显示模型配置或另一人的评分。由于第一版没有账号系统，协调人需要隔离文件访问；本机不同文件夹不是严格的安全隔离。如果回答主动暴露模型身份，记录这项盲评限制。

开放题五维各 0–4 分，评分者必须写依据。关键错误在相关维度处理，不能同时无依据地扣多个维度。若同维度差至少 2 分，或总分差超过 10 个百分点，第三人裁定。刚好 10 个百分点且所有维度差都小于 2 时，取均值。来源/结论正确性及拒答判断不一致也交裁定。

第三位专家填写单独的 JSON，按原始题号索引。例如实验设计题：

```json
{
  "EXAMPLE-ID": {
    "reviewer": "mol-c",
    "scores": {"hypothesis_measurement": 3, "controls": 2, "replication_statistics": 3, "confounds_feasibility": 2, "interpretation": 3},
    "rationale": "替换为第三位专家结合回答、细则和原始分歧写出的裁定理由。",
    "source_correct": null,
    "conclusion_correct": null,
    "refusal": false
  }
}
```

论文辨析题的 `source_correct` 和 `conclusion_correct` 必须分别填写 `true` 或 `false`；它们表示对模型该项判断是否正确的专家评价。第三人需使用该题能力对应的五个维度，并与前两位不同。

```console
lsrw score --run RUN_DIRECTORY --keys PRIVATE/keys.json --reviews PRIVATE/reviews/round-1 --adjudications PRIVATE/adjudications.json
```

前两人的原始评分不会被覆盖。修订评分细则则创建新评分轮次和新版本，保留原有记录。正式评测还会检查评分者是否属于锁定名册。

## 发布前

核对报告中的完整性、正式榜单资格、题量和置信区间。不要将模拟回答、草稿题结果或未完成评分的报告当作正式能力排名。使用发布文件清单打包；保留题、密钥、答案、专家身份和未公开回答始终留在私有目录。
