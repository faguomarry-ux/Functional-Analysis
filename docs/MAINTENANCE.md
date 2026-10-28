# 当前状态与维护记录

维护日期：2026-10-28（北京时间）。本页集中记录当前入口与本次工程维护；各章数学论证的范围以正文和对应 COVERAGE 为准。

## 当前讲义

| 项目 | 当前状态 |
| --- | --- |
| 统一源码入口 | [main.tex](../main.tex) |
| 主线 | 吉田第 0–14 章，132/132 个编号节已有首轮正文，含第五、十章附录 |
| 专题 | 广义函数第 15–22 章，共八章 |
| 习题与答案 | 主线 236 份、专题 21 份，共 257 份 |
| 书末 | 版本与教材对照、补充说明、集中答案、书目与引文追溯、105 条索引及记号表 |
| 最新本地 PDF | `output/pdf/main.pdf`；由完整入口三遍编译生成，不纳入 Git |
| 待办 | 独立数学审校、各章明确保留的证明边界、汪林反例索引 |

## 文档导航

- [README](../README.md)：项目概况、阅读与构建入口。
- [PROGRESS](PROGRESS.md)：当前进度、审校待办与历史时间线。
- [CONTRIBUTING](../CONTRIBUTING.md)：写作、验证、文档同步及清理约定。
- [第三方材料说明](../THIRD_PARTY_NOTICE.md)：教材、模板、字体的来源和待核对事项。
- [教学插图说明](../figures/README.md)：13 幅 TikZ 图的索引和维护方法。
- 主线逐章覆盖记录：[0](../books/yosida/chapter00/COVERAGE.md)、[1](../books/yosida/chapter01/COVERAGE.md)、[2](../books/yosida/chapter02/COVERAGE.md)、[3](../books/yosida/chapter03/COVERAGE.md)、[4](../books/yosida/chapter04/COVERAGE.md)、[5](../books/yosida/chapter05/COVERAGE.md)、[6](../books/yosida/chapter06/COVERAGE.md)、[7](../books/yosida/chapter07/COVERAGE.md)、[8](../books/yosida/chapter08/COVERAGE.md)、[9](../books/yosida/chapter09/COVERAGE.md)、[10](../books/yosida/chapter10/COVERAGE.md)、[11](../books/yosida/chapter11/COVERAGE.md)、[12](../books/yosida/chapter12/COVERAGE.md)、[13](../books/yosida/chapter13/COVERAGE.md)、[14](../books/yosida/chapter14/COVERAGE.md)。
- 历史复核：[第 0–3 章与插图](REVIEW-CH00-03.md)、[2026-10-26 快审](REVIEW-2026-10-26.md)、[专题与书末](REVIEW-PART-II-BACKMATTER.md)。

## 本次清理与文档同步

清理前工作区无未提交改动。逐项核对 Git 跟踪清单后，将 **2,663 个文件，共 690,958,227 字节（约 658.95 MiB）**移入系统回收站，包括 `tmp/` 中的截图、一次性脚本和历史日志，`output/` 中的旧 jobname 讲义、旧校验文件和辅助文件，以及根目录旧 `main.pdf`、正文目录残留 `.aux`。需要时可从系统回收站恢复。

五本参考 PDF、所有 Git 跟踪文件、模板、TikZ 源码、本地字体和 `output/pdf/main.pdf` 均保留。空临时目录可供后续工作继续使用。完整重编译会重新生成必要的辅助文件，这些文件继续由 `.gitignore` 排除。

同步已有的 **23 份 Markdown 文档**，新增本维护记录。README 明确历史计划与当前审校目标；PROGRESS 修正首轮正文已完成而任务框仍未勾选的条目；写作、权利与插图文档补充维护范围；十五份 COVERAGE 和三份复核记录增加当前状态入口，保留原始阅读范围、页数及证明边界。

本轮为文件和项目文档维护，没有新增数学结论或独立审校结论。历史记录中的旧 PDF 文件名是当时的验收标识，当前统一阅读入口以本页为准。

## 本次验证

- `scripts/check-sources.py` 通过：179 个实际装载的 TeX 文件，标签、引用、引文及环境检查通过，132/132 个主线编号节已有正文。
- 核对源码中的习题与解答总数，均为 257。
- 检查全部 24 份 Markdown 文档中的 112 个本地文件链接，目标均存在。
- 清理辅助文件后，`build-book.ps1` 完整三遍 XeLaTeX 构建通过，最终 `output/pdf/main.pdf` 为 **436 页**。
- 最终日志无未定义引用或引文、重复标签、Overfull 或缺字；保留五处 Underfull 提示。本轮未改动排版或数学正文，历史人工页面验收仍以原记录为准。
- `git diff --check` 通过。生成文件继续被忽略；本次普通文档提交不包含 Release 触发关键词。远端 Actions 的运行状态以对应提交的 GitHub 构建记录为准。
