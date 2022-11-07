# continue演示
for i in range(3):
    if i == 1:
        continue
    print(f"循环内i={i}")
print("循环执行完毕")

print("---------")
# break演示
for i in range(3):
    if i == 1:
        break
    print(f"循环内i={i}")
print("循环执行完毕")

