def ing(str):
    st=str+"ing"
    print(st)
def ly(str):
    s=str+"ly"
    print(s)
str=input("enter the string : ")
g=str[-3]+str[-2]+str[-1]
y=str[-2]+str[-1]
if g=="ing":
    ly(str)
else :
    ing(str)
