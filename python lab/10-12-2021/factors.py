def factors(num):
    n=num
    for i in range(1,n+1,+1):
        if num%i==0:
            print(i)
num=int(input("enter the number :"))
factors(num)