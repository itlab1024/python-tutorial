i = 1
j = 2


# add函数，求两个数的和
def add(x, y):
    return x + y


print(add(i, j))  # 3


# 无参无返回值
def print_msg():
    print("hello python")


print(type(print_msg()))  # <class 'NoneType'>


def func_comment(a, b):
    """
    函数的说明写在这里
    :param a: 每个参数的说明写在这里
    :param b: 每个参数的说明写在这里
    :return: 返回值的说明写在这里
    """
    print("这是函数体")


# 函数中变量作用域
def result():
    r = 1
    print(r)


# print(r)  # 次数是获取不到变量r的

# 多返回值
def compute(x, y):
    return x + y, x - y


r1, r2 = compute(1, 2)
print(r1)  # 3
print(r2)  # -1

# 参数的传递方式
compute(x=1, y=2)


# 函数参数
# 我可以在定义一个参数，参数的类型是一个函数。
def func_params(compute):
    return compute(1, 2)


print(func_params(compute))  # (3, -1)

# 匿名函数
# 上面的函数就可以使用匿名函数调用
print(func_params(lambda x, y: x + y))  # 3
