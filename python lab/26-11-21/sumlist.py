n=int(input("enter the limit : "))
list=[]
sum=0
print("enter the elements of list : ")
for i in range(n):
    num=int(input())
    list.append(num)
    sum=sum+num
print("the given list is : ",list)
print("the sum of the elements in list is : ",sum)