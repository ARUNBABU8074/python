import math
def digit(s,e):
    c=0
    for i in range(s,e+1,+1):

        num=math.sqrt(i)
        n=num*num
        if n==i:
            while n>0:
                r=n%10
                if r%2==0:
                    c=c+1
                p=r/10
                n=(n/10)
            if c==4:
                 print(i)
s=int(input("enter the start : "))
e=int(input("enter the end : "))
digit(s,e)
