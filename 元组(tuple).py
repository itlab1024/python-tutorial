# 定义元组
from filecmp import cmp

t1 = (1, "python", 1.24)
# 特别注意如果元组之后一个元素，不能忽略后面的逗号
t2 = (2,)
print(type(t2))  # <class 'tuple'>
# 获取元组，使用下标获取元素
print(t1[0])  # 1
# 元组是不能修改元素的，但是可以将两个元组组合到一起
t3 = t1 + t2
print(t3)  # (1, 'python', 1.24, 2)

# 元组运算符*
t4 = (1,)
print(t4 * 3)  # (1, 1, 1)
# 判断元素是否存在于元组中
print(1 in t4)  # True

# 循环
for i in t4:
    print(i)  # 1

# 截取元组
t5 = (1, 2, 3, 4)
# 只用冒号则结果跟原元组一样
print(t5[:])  # (1, 2, 3, 4)
# 截取第二个到尾部
print(t5[1:])  # (2, 3, 4)
# 可以使用负数
print(t5[1: -1])  # (2, 3)
# 也可以指定步长
print(t5[1:1:1])  # 3

# 元组简化定义方法
t6 = 1, 2, 4, ("a", 1)
print(type(t6))  # <class 'tuple'>
# 元组的比较
t7 = (1, 2)
t8 = (2, 1)
print(t7 > t8)  # Flase
print(t7 < t8)  # True
print(t7 == t8)  # False

# 获取元组中最大值与最小值
print(min(t7))  # 1
print(max(t8))  # 2

# 列表转化为元组
t9 = tuple([1, 2, 4])
print(type(t9))  # <class 'tuple'>
print(t9)  # (1, 2, 4)
# 将元组转化为list
t10 = list(t9)
print(type(t10))  # <class 'list'>
print(t10)  # [1, 2, 4]

# 元组长度
print(len(t9))  # 3
