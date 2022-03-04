n = int(input("Enter the limit"))
print("Enter the value")
list=[]
for i in range (0,n):
    num = int(input())
    if(num>100):
        list.append("over")
    else:
        list.append(num)
print(list)