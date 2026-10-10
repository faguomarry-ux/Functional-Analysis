# 泛函分析：吉田第六版主线与广义函数专题

[![Build notes and release](https://github.com/faguomarry-ux/Functional-Analysis/actions/workflows/build-release.yml/badge.svg)](https://github.com/faguomarry-ux/Functional-Analysis/actions/workflows/build-release.yml)

以吉田耕作《泛函分析》第六版中译本为学习主线，英文原版辅助核对术语、目录与页码，结合施瓦尔茨、盖尔芳特与希烙夫的广义函数著作，以及汪林的反例教材，逐步整理中文个人学习讲义。正文使用 LaTeX 编写，统一符号、证明、例子和习题解答。

**本项目仅用于个人、非商业学习，不开展教材销售、付费课程或其他商业活动。** 项目仍在编写和校对中：目前已有第零至第三章正文及八章广义函数专题，主线第四至十四章仍为占位。编译成功只表示排版构建通过，不表示数学内容已经全部完成或正确。

更新时间：**2026-10-11（北京时间）**。

## 阅读入口

- [学习讲义快照 / Releases](https://github.com/faguomarry-ux/Functional-Analysis/releases)：自动编译的 PDF 与 SHA-256 校验文件，快照标记为预发布。
- [Actions 构建记录](https://github.com/faguomarry-ux/Functional-Analysis/actions)：普通提交的讲义产物及失败日志；Artifacts 下载通常需要登录 GitHub。
- [详细进度与时间线](docs/PROGRESS.md)：逐章状态、阶段目标、完成标准、项目待办及更新记录。
- [贡献与写作规范](CONTRIBUTING.md)：章节组织、引用、习题、校对与提交约定。
- [个人非商业学习许可](LICENSE) / [第三方材料说明](THIRD_PARTY_NOTICE.md)：原创内容与教材、译文、模板、字体的许可边界。

## 五本参考教材

五个 PDF 文件保留在仓库根目录，`.gitignore` 不使用 `*.pdf` 通配忽略规则。表中路径按现有文件名记录，未修改原文件名。

| 教材 | 作者 / 译者 | 本项目用途 | 文件 |
| --- | --- | --- | --- |
| 《泛函分析》第六版中译本 | 吉田耕作（Kōsaku Yosida）；译者信息待核对版权页 | 主线章、节顺序及中文页码 | [中译本](<泛函分析 第6版 (吉田耕作) 中译本.pdf>) |
| Functional Analysis, Sixth Edition | Kōsaku Yosida | 英文术语、公式、版本和页码交叉核对 | [英文原版](<泛函分析 第6版 英文原版.pdf>) |
| 《广义函数论》 | Laurent Schwartz 著，姚家燕译 | 测试函数、分布及基本运算 | [广义函数论](<广义函数论 法兰西数学精品译丛 (L.施瓦尔茨,姚家燕).pdf>) |
| 《广义函数 III：微分方程理论的若干问题》 | I. M. Gelfand、G. E. Shilov | 加权空间、柯西问题与广义固有函数 | [广义函数 III](<广义函数 Ⅲ 微分方程理论的若干问题 (（苏）и.М.盖尔芳特 г.Е.希烙夫) .pdf>) |
| 《泛函分析中的反例》 | 汪林 | 后续补充条件辨析、反例及习题；尚未系统整合 | [反例教材](<泛函分析中的反例 (汪林.pdf>) |

教材、扫描件及译文的版权属于各自权利人，本项目的 LICENSE 不对它们重新授权。**五本教材的公开上传授权尚未在本仓库中核实；公开上传前须确认相应授权或其他合法依据。** “个人学习”“非商业”声明不自动赋予第三方教材的公开传播权；私有仓库也不改变材料本身的权利归属。相关记录见 [第三方材料说明](THIRD_PARTY_NOTICE.md)。

当前五本参考 PDF 合计约 243.9 MiB，最大文件约 90.7 MiB。GitHub 对超过 50 MiB 的普通 Git 文件给出提示，对超过 100 MiB 的文件予以阻止；浏览器上传单文件限制为 25 MiB，因此本批文件应通过 Git 上传。当前未强制引入 Git LFS，替换为更大文件前重新检查大小。[GitHub 大文件说明](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)

## 内容范围与当前进度

第一部分保留吉田原书 **第 0–14 章，共 15 章、132 个编号节**。第零章四节、第一章十四节、第二章七节及第三章十一节已有正文和核查记录，合计 **36/132 节，约 27.3%**；这是已有正文的节数比例，不代表阅读比例、工作量比例或最终校对完成率。第五、十章的原书附录保留在各自章末。

| 模块 | 当前状态 | 下一步 |
| --- | --- | --- |
| 第零章：预备知识 | 四节正文及章末文献已整理，8 道附解答习题 | 复核证明边界、引文与交叉引用 |
| 第一章：半范数 | 十四节正文已整理，8 道附解答习题 | 二轮数学校对与排版检查 |
| 第二章：Baire–Hausdorff 定理的应用 | 七节正文、证明、例子及 8 道附解答习题已整理 | 二轮独立数学校对与后续章节衔接 |
| 第三章：正交投影及 F. Riesz 表示定理 | 十一节正文、证明、例子及 11 道附解答习题已整理 | 本轮数学检查与完整排版验收见 COVERAGE；后续独立复核 |
| 第四至十四章 | 96 个编号节保留标题、两版页码和占位提示 | 从第四章开始逐节补写 |
| 广义函数专题：第 15–22 章 | 八章已有正文、证明、例子和习题 | 逐章复核与主线的衔接及出处 |
| 版本对照与参考对照 | 已有附录框架与主要映射 | 随正文补写更新 |
| 补充说明、索引、空间记号表、原书总书目 | 仍有占位；第零章相关五组文献已核对 | 整理实际引用、生成可检索索引 |
| 汪林反例专题 | 参考书已列入，未系统整合 | 按定理条件建立反例索引 |
| GitHub 工程配置 | 忽略规则、许可证、构建/发布工作流和项目文档已写入 | 第二章 Release 已验证，继续维护后续阶段快照 |

核查依据见 [第零章 COVERAGE](books/yosida/chapter00/COVERAGE.md)、[第一章 COVERAGE](books/yosida/chapter01/COVERAGE.md)、[第二章 COVERAGE](books/yosida/chapter02/COVERAGE.md)、[第三章 COVERAGE](books/yosida/chapter03/COVERAGE.md) 和 [目录数据](books/yosida/catalog.json)。不把目录、占位或仅有编译产物的章节计为完成。

## 时间线与近期待办

以下为 **2026-10-10 制订的建议计划**，按个人学习时间和章节难度滚动调整，日期不是已完成记录或硬性承诺。完整分解见 [PROGRESS.md](docs/PROGRESS.md)。

| 时间（北京时间） | 阶段 | 计划验收成果 |
| --- | --- | --- |
| 2026-10-10—10-18 | 仓库与既有内容基线 | 核对第三方材料权利；验证 GitHub 构建和一次 Release；复核第 0、1 章 |
| 2026-10-19—11-15 | 基本定理 | 补写第 2–4 章，核对条件、证明、例子及习题 |
| 2026-11-16—12-13 | 收敛与对偶 | 补写第 5、7 章及第 5 章附录 |
| 2026-12-14—2027-01-10 | Fourier 与分布衔接 | 补写第 6 章，复核专题第 15–20 章 |
| 2027-01-11—02-14 | 算子与谱 | 补写第 8–11 章及第 10 章附录；该阶段工作量较大 |
| 2027-02-15—03-21 | 表示与发展方程 | 补写第 12–14 章，复核专题第 21、22 章 |
| 2027-03-22—04-18 | 反例、附录与全书校对 | 整合汪林反例；补齐索引、符号表与书目；发布阶段总结 |

近期待办：

- [ ] 核对五本教材的版权页、译者、版本及公开传播依据，记录在第三方材料说明中。
- [ ] 核对 maki-notes 模板来源及许可；本地字体副本默认不提交。
- [x] 工程文件已推送到 GitHub，初始 Actions 构建成功（2026-10-10）。
- [x] 第二章 `[release]` 发布成功，已核验下载 PDF 与 SHA256（2026-10-11）。
- [ ] 按第零、第一章 COVERAGE 完成第二轮校对，不提前把校对状态标为完成。
- [x] 补写第二章七节，更新核查记录并加入 8 道附解答习题（2026-10-11）。
- [x] 补写第三章十一节与 11 道附解答习题，记录数学自查与证明边界（2026-10-11）。
- [ ] 完成第二、三章二轮独立数学校对，继续第四章。
- [ ] 建立反例索引，标明每个反例针对哪个定理条件。

## 仓库结构

```text
.github/workflows/build-release.yml  提交/PR 构建与关键词发布
.gitignore                         忽略构建输出，保留参考教材 PDF
.gitattributes                     文本换行与二进制文件规则
LICENSE                            自定义个人非商业学习许可
THIRD_PARTY_NOTICE.md               教材、模板、字体的权利说明
CONTRIBUTING.md                     写作与校对规范
docs/PROGRESS.md                    详细进度、时间线和项目待办
main.tex                           封面、目录、分部、章节、附录与答案
functional-analysis.sty            本项目符号与排版设置
maki-notes.cls / maki-notes.sty      既有讲义模板
books/
  yosida/00-...14-*.tex              吉田第 0–14 章入口
  yosida/chapter00/                 第零章逐节正文与 COVERAGE.md
  yosida/chapter01/                 第一章逐节正文与 COVERAGE.md
  yosida/chapter02/                 第二章逐节正文与 COVERAGE.md
  yosida/chapter03/                 第三章逐节正文与 COVERAGE.md
  yosida/catalog.json               两版目录、节名与原书页码
  yosida/15-...18-*.tex              版本对照、补充说明、索引及记号表
  00-preface.tex                    前言和数学约定
  01-motivation.tex ... 08-weighted-spectral.tex
                                   广义函数专题八章
  09-reference-map.tex              专题参考书对照
  10-bibliography.tex               统一文献表
figure/                            插图资源
scripts/build-book.sh               Linux/macOS 完整编译入口
build-book.ps1 / build.bat          Windows 编译入口
五本教材 PDF                       参考资料，使用原有文件名
output/pdf/main.pdf                 本地编译输出（忽略）
fonts/、tmp/                        本地字体与临时资料（忽略）
```

## 本地编译

源文件使用 UTF-8，主入口为 `main.tex`，编译引擎为 **XeLaTeX**。安装包含中文支持与常用宏包的 TeX Live 或 MiKTeX，并确保 `xelatex` 在 PATH 中。主要依赖包括 ctex、fontspec、tcolorbox、tikz、pgfplots、amsmath、mathtools 和模板加载的其他宏包。

Windows PowerShell：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\build-book.ps1
# 或在命令提示符执行 build.bat book；双击 build.bat 也默认编译本书。
```

Linux / macOS（已安装 TeX 环境）：

```bash
bash scripts/build-book.sh
```

两个脚本均连续编译三遍，以稳定目录、交叉引用与页码。讲义 PDF、日志及辅助文件位于 `output/pdf/`。`.gitignore` 排除该目录及根目录旧的 `main.pdf`，因此阅读时应使用新编译结果或对应 Release。

GitHub Actions 在 Ubuntu 上安装 texlive-xetex、texlive-lang-chinese、texlive-latex-extra、texlive-fonts-recommended、texlive-science、texlive-pictures。`fontpreset=auto` 按平台选择字体：Windows 优先系统中文字体；Linux 无适配字体时退回 TeX 自带的 Fandol。不同平台的字体可能造成分页差异。编译不依赖五本参考 PDF，也不依赖本地 `fonts/`。

原脚本保留了 example 和 all 参数，但当前仓库没有 `example.tex`；目前使用默认 book 目标即可。索引仍为占位，当前流程不调用 makeindex。

## GitHub 自动构建与 Release

工作流位置是 **`.github/workflows/build-release.yml`**。

| 触发方式 | 自动行为 |
| --- | --- |
| 向任意分支推送提交 | 完整编译，上传 lecture-notes 构建产物 |
| Pull Request | 完整编译和产物上传 |
| 默认分支最新提交的信息含 `[release]` | 构建成功后自动发布讲义预发布快照 |
| Actions → Build notes and release → Run workflow | 默认仅编译；勾选 publish_release 且选择默认分支时发布 |

例如已有首次提交、默认分支及 GitHub 用户配置后：

```powershell
git add README.md docs books main.tex functional-analysis.sty
git commit -m "docs: 完成第三章学习笔记 [release]"
git push
```

关键词只检查一次 push **最末提交**的完整信息（标题和正文）；把关键词放在较早提交中不会触发发布。只从仓库默认分支发布，普通分支与 PR 只构建。采用 squash merge 时应保留最终合并提交中的 `[release]`。避免同时写 `[skip ci]` 等跳过工作流指令。

自动标签为 `notes-<完整提交 SHA>`，绑定实际编译的提交。同一提交已经发布时，重跑发布步骤会跳过，避免重复 Release。更新讲义请提交新版本再触发发布。Release 附件包含：

- `functional-analysis-notes.pdf`：完整学习讲义。
- `SHA256SUMS.txt`：附件校验值。

教材 PDF 留在 Git 资料范围，工作流仅检出构建源文件和插图；Release 附件不额外打包教材。GitHub 自动提供的 Source code 压缩包仍可能包含 Git 已跟踪的教材，公开仓库前同样要核对其传播依据。

讲义 Artifact 保留 30 天，诊断日志保留 7 天；仓库或组织策略可能进一步限制期限。构建失败时不发布，优先下载 latex-diagnostics 查看 main.log。发布步骤使用 GitHub 自动提供的 GITHUB_TOKEN，仅该 job 获得 contents: write，无需手工添加 PAT。仓库/组织须允许 Actions 运行及相应写权限。[GitHub Token 文档](https://docs.github.com/en/actions/tutorials/authenticate-with-github_token)

## 首次上传与日常维护

仓库远端已配置为 `faguomarry-ux/Functional-Analysis`，项目使用 main 分支。以下命令将 main 推送到远端并建立跟踪关系。

确认五本教材的上传依据，并核对将要纳入的文件后，在 PowerShell 执行：

```powershell
git status --short
git add --dry-run .
# 核对清单后执行：
git add .
git commit -m "chore: 初始化个人泛函分析学习项目"
git push -u origin main
```

首次 `git add .` 会纳入五本参考 PDF、正文和工程文件，并排除 fonts/、tmp/、output/ 及生成文件。Git 提交需要事先配置 user.name 与 user.email，SSH 远端需要可用的 GitHub 密钥配置。手工触发工作流前，工作流文件应已存在于 GitHub 默认分支。

之后按学习单元提交，采用 notes:、fix:、docs:、ci: 等简洁前缀。日常记录不加发布关键词；阶段学习成果才加 `[release]`。每次补写后同步更新 [PROGRESS.md](docs/PROGRESS.md) 与相应 COVERAGE，避免文档状态落后于正文。

## 写作和数学约定

1. 吉田主线章号保留 0–14，广义函数专题顺接 15–22；不要在子章节中手工重置章号。
2. 新正文只写章节内容，不重复 documentclass 或 document 环境；章级入口用 include，章内拆分用 input。
3. 每节补写后移除对应 YosidaSectionPlaceholder；全章完成后再移除章占位，并更新覆盖核查。
4. 保留全局唯一标签，例如 `thm:banach-open`；最终发布完整编译，避免残留 includeonly。
5. 补充习题使用 exercise，解析用紧随其后的 solution；当前设置 answers=true,solutions=appendix，解答集中在书后。
6. 页码区分原书印刷页、PDF 页序与本稿自动页码；引文注明实际查阅范围，区分原书论证和本稿补充。

内积对第一变量线性；分布配对对测试函数线性，不混入 Hilbert 内积的复共轭。Fourier 变换采用 `exp(-i x·ξ)`，逆变换带 `(2π)^(-n)`，查阅不同教材时核对正负号与常数。一般严格 LF 空间定理、经典 Fourier 反演、Plancherel、Lax–Milgram 等已有结论的使用边界按正文和 COVERAGE 说明；未展开的证明不标为已经证明。

## 使用许可

本项目采用 [自定义个人非商业学习许可](LICENSE)，仅对贡献者有权许可的原创内容授予个人下载、复制、编译、阅读与私下修改的权限；保留署名、出处、许可及修改说明。商业使用、公开再分发等超出范围的使用须另获相关权利人许可。本项目采用限制性许可，不标称为 OSI 意义上的开源项目。

教材、译文、扫描件、既有模板与字体适用各自的权利和许可，不因仓库声明改变归属。发现引用、署名、许可或内容问题时，可通过 [Issues](https://github.com/faguomarry-ux/Functional-Analysis/issues) 提供具体文件与位置，维护者核实后更正或移除相关材料。

## 致谢

感谢 **吉田耕作（Kōsaku Yosida）**，其《泛函分析》第六版为本项目提供了系统的学习主线；感谢 **Laurent Schwartz（施瓦尔茨）**，其广义函数理论著作为分布专题提供了基础；感谢 **I. M. Gelfand（盖尔芳特）** 与 **G. E. Shilov（希烙夫）**，其《广义函数》系列将函数空间、微分方程与谱理论联系起来；感谢 **汪林**，《泛函分析中的反例》为理解定理假设与边界提供了重要参考。

同时感谢 **姚家燕** 及各书的译者、编辑、出版人员，以及相关数学理论的建立者。尚未核实的译者与版本信息将在核对版权页后补齐。感谢既有 maki-notes 模板的原作者，以及 TeX、LaTeX、CTeX 和各宏包维护者提供的排版工具。所有致谢均不表示原作者对本项目提供授权、审校或背书；原著与译文的权利仍归各自权利人。
