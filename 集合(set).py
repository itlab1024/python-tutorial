# 定义set
s1 = {1, 2, 3}
print(f"s1的类型是{type(s1)},，值是{s1}")  # s1的类型是<class 'set'>,，值是{1, 2, 3}
# 也可以使用set函数，传递一个集合（比如List）进行创建
l1 = [1, 2, 1]
s2 = set(l1)
print(f"s2的类型是{type(s2)},，值是{s2}")  # s2的类型是<class 'set'>,，值是{1, 2}

# 添加元素
s3 = {1}
s3.add(1)
s3.add(2)
print(s3)  # {1, 2}

# 删除元素
s3.remove(2)
print(s3)  # {1}

# 清空元素
s3.clear()
print(s3)  # set()

# 拷贝元素
s4 = {1}
s5 = s4.copy()
print(s4)  # {1}
print(s5)  # {1}
# 给s5增加个2
s5.add(2)
print(s4)  # {1}
print(s5)  # {1, 2}
