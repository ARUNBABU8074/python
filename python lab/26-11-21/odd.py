n=int(input("enter the limit : "))
list=[]
new=[]
print("enter the elements of list of integers : ")
for i in range(n):
    num=int(input())
    list.append(num)
print("the given list is : ",list)
for i in list:
    if i%2!=0:
        new.append(i)
print("the list without even number is : ",new)
