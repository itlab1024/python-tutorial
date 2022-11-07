# 定义字典
d1 = {"k1": "v1"}
print(f"d1的类型是{type(d1)}, 值是{d1}")  # d1的类型是<class 'dict'>, 值是{'k1': 'v1'}
# 添加
d1["k2"] = 1
print(d1)  # {'k1': 'v1', 'k2': 1}
# 删除
del d1["k1"]
print(d1)  # {'k2': 1}
# 修改
d1["k2"] = 2
print(d1)  # {'k2': 2}
# 查询
print(d1["k2"])  # 2

a = [1, 2]
print(a[1:2:1])
