# -*- coding:UTF-8 -*-
# 30道python基本入门小练习

# 1. 重复元素判定
# 以下方法可以检查给定列表是不是存在重复元素，它会使用 set() 函数来移除所有重复元素


def all_unique(lst):
    return len(lst) == len(set(lst))


x = [1, 2, 2, 3, 4]
y = [1, 2]
print(all_unique(x))
print(all_unique(y))
print("-----------")

# 2. 字符元素组成判定
# 检查两个字符串的组成元素是不是一样的。

from collections import Counter


def fs(first, second):
    return Counter(first) == Counter(second)


print(fs("ssa", "ass"))
print("-------------")

# 3. 内存占用
# 下面的代码块可以检查变量 value 所占用的内存

import sys
value = 1
print(sys.getsizeof(value))
print("------------------")


# 4

# 5
d = {'a': 1, 'b': 2}
print(d.get('c', 3))
