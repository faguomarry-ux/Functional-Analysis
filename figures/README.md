# 第 0–3 章教学插图

所有插图均为本项目绘制的 TikZ 矢量图，源文件集中在本目录，由正文 `\input{figures/…}` 载入。共用样式在 `tikz-styles.tex`，由 `functional-analysis.sty` 加载；使用现有主题颜色，编译不需要外部绘图程序或 shell escape。

| 文件 | 解释的关键步骤 |
| --- | --- |
| ch00-urysohn.tex | 闭包嵌套与指标下确界 |
| ch00-baire.tex | 嵌套闭球、中心 Cauchy 与完备性 |
| ch01-seminorm.tex | 半范数零空间与有限交邻域 |
| ch01-test-support.tex | 支集逃逸与共同紧支集条件 |
| ch01-quotient.tex | 改变代表元与距离下确界 |
| ch02-uniform-boundedness.tex | 从非零中心内球移到零附近 |
| ch02-open-mapping.tex | 可求和修正与残差趋零 |
| ch02-closed-graph.tex | 图像空间的两个投影 |
| ch03-projection.tex | 正交分解与最近点 |
| ch03-ascoli.tex | 有限网点控制与三段误差 |
| ch03-radon-nikodym.tex | 共同测度与密度换算 |
| ch03-reproducing-kernel.tex | 点值约束下的最小范数 |
| ch03-local-structure.tex | 高阶导数、闭子空间 Riesz 表示与限制域 |

图的 label、caption 与 tikzpicture 一并保存在插图文件内。正文在对应证明后说明图的用途，并用全局唯一的 `fig:y…` 标签引用；不在图中推进定理计数器。

维护时检查：箭头代表的是映射、集合关系还是误差估计；开球边界是否误画为包含；二维示意是否掩盖完备性、闭性、复标量或局部范围假设。图不能替代证明，也不把一般 Banach 空间误画成具有正交投影的空间。新增图后完整编译三遍并查看图所在 PDF 页及前后页面。

维护同步（2026-10-28）：13 幅教学插图及共用样式均保留，正文仍直接载入 TikZ 源文件。临时渲染截图不作为插图源文件；需要检查时从完整讲义重新渲染。全书当前输出和验收边界见[维护记录](../docs/MAINTENANCE.md)。
