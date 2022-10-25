# 整数类型
i = 1
print(i)  # 1
# 如果数字比较长，可以使用_分割
j = 100_24
print(j)  # 10024

# 浮点型
a = 1.1
print(a)
b = -1.2
print(b)

# 复数,复数的格式是 a + bj(J)
c1 = 1 + 3j
print("c1的类型是", type(c1), "值是", c1)  # c1的类型是 <class 'complex'> 值是 (1+3j)

# --------布尔类型--------
b1 = True
b2 = False

# -------------字符串-------------
s = "a"  # 使用双引号括起来的是字符串
print(s)
s1 = '学习python'  # 也可以使用单引号
print(s1)
s2 = """
我
在
学习
python
"""  # 可以使用三引号，三引号是允许换行的，并且保留格式
print(s2)

# -------------List类型-------------
l1 = [1, 2]
print("l1的类型是", type(l1), "值是", l1)  # l1的类型是 <class 'list'> 值是 [1, 2]
# 可以存储任意类型
l2 = [1, "曹操", 1.2, 1 + 2j]
print("l2的类型是", type(l2), "值是", l2)  # l2的类型是 <class 'list'> 值是 [1, '曹操', 1.2, (1+2j)]

# 通过下标修改，下标index从0开始
l2[0] = 10
print("l2的类型是", type(l2), "值是", l2)  # l2的类型是 <class 'list'> 值是 [10, '曹操', 1.2, (1+2j)]
# 以下修改会出错，因为l2下标目前对打是3，没有4，所有提示找不到。IndexError: list assignment index out of range
# l2[4] = -1
# print("l2的类型是", type(l2), "值是", l2)
# 增加元素
l2.append("刘备")
print(l2)  # [10, '曹操', 1.2, (1+2j), '刘备']
# 删除元素
del l2[len(l2) - 1]
print(l2)  # [10, '曹操', 1.2, (1+2j)]

