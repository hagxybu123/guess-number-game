import random

# 随机生成1~100数字
answer = random.randint(1, 100)
count = 0
print("====猜数字游戏====")
print("我已经想好1~100之间一个数字，你来猜！")

while True:
    try:
        num = int(input("请输入你的猜测："))
        count += 1
        if num > answer:
            print("大了")
        elif num < answer:
            print("小了")
        else:
            print(f"恭喜！猜中了！一共猜了{count}次")
            break
    except ValueError:
        print("请输入合法整数！")