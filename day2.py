import random
import time
jb = 5000
sj = 0
randint = random.randint(1,50)
while True:
    num = input("请输入一个数字")
    if num.isdigit():
        num = int(num)
        if num > randint:
            print("猜大了")
            jb = jb - 500
            sj = sj + 1
            print("剩余金币为:",jb)
            if sj % 3 == 0:
                print("别瞎猜了")
                time.sleep(10)
            if sj == 10:
                print("当前金币为0，少年该充钱了")
                break
            continue
        if num < randint:
            print("猜小了")
            jb = jb - 500
            sj = sj + 1
            print("剩余金币为:", jb)
            if sj % 3 == 0:
                print("别瞎猜了")
                time.sleep(10)
            if sj == 10:
                print("当前金币为0，少年该充钱了")
                break
            continue
        else:
            print("猜对了,获得金币3000")
            jb = jb + 3000
            print("当前金币为:",jb)
            break


