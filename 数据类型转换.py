
# ------数据类型转换,转换为那种类型就用那种类型对应的函数，很方便记忆，比如转换为string，就使用str(),str是string的简写,转换为int就使用int()---------
# 整数、浮点数、布尔类型转换为字符串
s1 = str(1)  # 整数
print("s1的类型是", type(s1), "值是", s1)  # s1的类型是 <class 'str'> 值是 1
s2 = str("123.44")  # 浮点数
print("s2的类型是", type(s2), "值是", s2)  # s2的类型是 <class 'str'> 值是 123.44
s3 = str(True)  # 布尔
print("s3的类型是", type(s3), "值是", s3)  # s3的类型是 <class 'str'> 值是 True

# 字符串、浮点型、布尔类型等转化为整数，使用int()方法
i1 = int("11")
print("i1的类型是", type(i1), "值是", i1)  # i1的类型是 <class 'int'> 值是 11
# 不是所有的字符都能转化为整数，必须是数字字符串才可以
# i2 = int("中国")  # 转化不会成功，会提示错误ValueError: invalid literal for int() with base 10: '中国'，中国不是数字类型的字符串是没办法转化为数字的
# print("i2的类型是", type(i2), "值是", i2)
# 布尔类型转化为整数，True会被转化为1，False会被转化为0。
i2 = int(True)
print("i2的类型是", type(i2), "值是", i2)  # i2的类型是 <class 'int'> 值是 1
i3 = int(False)
print("i3的类型是", type(i3), "值是", i3)  # i3的类型是 <class 'int'> 值是 0
# 浮点数转化为整数,小数部分会被舍弃
i3 = int(1.2345)
print("i3的类型是", type(i3), "值是", i3)  # i3的类型是 <class 'int'> 值是 1
# 复数是不能转化为int的
# i3 = int(1 + 2j)  # 此处会执行错误，TypeError: int() argument must be a string, a bytes-like object or a real number, not
# 'complex'


# 字符串、整数转换为浮点数，非数字或者非浮点数样子的字符串是不能够转化为浮点数的。
f = float(12)
print("f的类型是", type(f), "值是", f)  # f的类型是 <class 'float'> 值是 12.0
f = float("235.33")
print("f的类型是", type(f), "值是", f)  # f的类型是 <class 'float'> 值是 235.33