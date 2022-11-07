l = range(5)
print(f"list的类型是{type(l)}")
for i in l:
    print(i)  # 结果是0，1，2，3，4

l = range(2, 5)
for i in l:
    print(i)  # 结果是[2, 3, 4]
print("------")
# 设置步长
l = range(1, 10, 2)  # 左开右闭区间[1, 10)内，按照步长等于2取值，结果是[1, 3, 5, 7, 9]
for i in l:
    print(i)
