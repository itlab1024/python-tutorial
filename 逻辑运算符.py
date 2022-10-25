j = False
if not j:
    print("j不等于True")

# and
i = False
if j and i:
    print("j和i都是true")  # 此处不会打印，因为j和i等于False，其实如果其中有一个等于False都不会打印

# or
k = True
if j or k:
    print("j或者k有一个是True，就会打印该语句")  # j或者k有一个是True，就会打印该语句