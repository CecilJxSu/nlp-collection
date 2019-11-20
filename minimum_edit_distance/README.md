# Edit distance

**编辑距离**是衡量 2 个字符串的相似程度。测量方式是将 1 个字符串通过有限次数的操作（删除 deletion、插入 insertion、替换 subtitution）变成另外 1 个字符串的过程，并且计算操作消耗的成本。

例如：intention --> execution

```
i n t e * n t i o n
| | | | | | | | | |
* e x e c u t i o n
d s s   i s
```

计算**编辑距离**的消耗成本（或称为权重）有多个版本，最简单的就是 **The Levenshtein distance**。以及编辑距离默认指的就是莱文斯坦距离。

# The Levenshtein distance:

**莱文斯坦距离**也有两个版本，分别是：

1. d, s, i 操作的成本都为 1。则上面的 distance = 5
2. 仅允许 d, i 操作，成本分别为 1。虽然不允许 s 操作，但 s 可以看成是 1 个 d 和 1 个 i，因此 s 为 2。所以上面的 distance = 8

# The minimum edit distance

如何寻找最小的编辑距离？我们可以将此当作是搜索任务，从一个字符串到另一个字符串的所有编辑序列中找出最短的路径。

![figure1](https://ceciljxsu.oss-cn-shenzhen.aliyuncs.com/nlp/minimum_edit_distance_fg1.svg)

但这样的编辑序列可能会很多，因此不能直接搜索。然而，很多不同的编辑序列都有相同的结束情形（字符串），于是，我们可以依次在有相同结束情形的序列中，找出最短的路径。我们可以使用动态规划的思想，即将原问题拆分为多个容易求解的小问题，然后分别求解小问题，最后求得原问题的解。

## 思路

已知两个字符串，源字符串 X 的长度为 n，目标字符串 Y 的长度为 m。我们定义 D(i,j) 为 X[1...i] 和 Y[1...j] 之间的编辑距离，例如：字符串 X 的前 i 个字符和字符串 Y 的前 j 个字符。因此，可得到字符串 X 和 字符串 Y 之间的编辑距离为 D(n,m)。

我们将使用动态规划自下而上的方法求得 D(n,m)。基础情形下，源字符串的子串长度为 i，但目标字符串的子串为空，从 i 个字符到 0 个需要 i 个删除操作。如果是目标字符串的子串长度为 j，但源字符串的子串为空，需要将 0 个字符变成 j 个字符需要 j 个插入操作。为了计算 i,j 子串的 D(i,j) 值，我们可以基于 i,j 更短一点的子串计算它的值，因此得到较长的 i,j 子串的 D(i,j) 值。

D(i,j) 的值可以通过计算 3 条可行的编辑路径的最小值得到，路径可以是以下这 3 种：

![equation1](https://ceciljxsu.oss-cn-shenzhen.aliyuncs.com/nlp/minimum_edit_distance_eq1.svg)

如果使用的是**莱文斯坦距离**版本，即删除和插入消耗 1 个单位的成本，而替换消耗 2 个单位的成本（除了相同字母替换的成本为 0）。因此，计算公式变成：

![equation2](https://ceciljxsu.oss-cn-shenzhen.aliyuncs.com/nlp/minimum_edit_distance_eq2.svg)
