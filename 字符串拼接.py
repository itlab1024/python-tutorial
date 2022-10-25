# 直接使用+来拼接
print("我正在学习" + "python")
# 如果有变量也直接拼接变量即可
greet = "大家好"
print(greet + "我正在学习" + "python")
# 字符串拼接其他类型，比如int
age = 20
# print(greet + "," + age + "的" + "我正在学习" + "python")  # age是int类型，直接拼接会报错，需要转化,使用str(int)函数
print(greet + "," + str(age) + "的" + "我正在学习" + "python")
