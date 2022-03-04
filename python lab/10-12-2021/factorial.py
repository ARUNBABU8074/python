def fact(n):
    f=1
    for i in range(n,0,-1):
        f=f*i

    print("factorial= ",f)
num=int(input("enter the number : "))
fact(num)