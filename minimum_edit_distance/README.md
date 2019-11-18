# Edit distance

**编辑距离**是衡量 2 个字串的相似程度。测量方式是将 1 个字串通过有限次数的操作（删除 deletion、添加 insertion、替换 subtitution）变成另外 1 个字串的过程，并且计算操作消耗的成本。

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
