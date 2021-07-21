import random
m=int(input("请输入一个数: "))
count=0
while True:
    n=random.randint(0,9)
    if m > n:
        print("猜大了，请再猜一次")
        count+=1
    elif m<n:
        print("猜小了,请再猜一次")
        count+=1
    else:
        count+=1
        if 0<count<=3:
            print("你在第"+str(count)+"次猜对了")
        elif 4<=count<=8:
            print("你终于在第"+str(count)+"次猜对了")
        else:
            continue
        break


