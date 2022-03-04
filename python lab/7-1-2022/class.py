class rec:
    def __init__(self,l,b):
        self.length=l
        self.width=b
    def area(self):

        return (self.length*self.width)


    def per(self):
        perimeter = 2 * (self.length+self.width)
        print("perimeter of rectangle is : ", perimeter)
    def comp(self,x):
        if(self.area() == x.area()):
            print("they are equal")
        else:
            print("not equal ")

l=int(input("enter the length of the first rectangle : "))
b=int(input("enter the breadth of the first rectangle : "))
obj=rec(l,b)
print("area : ",obj.area())

obj.per()
l2=int(input("enter the length of the second rectangle : "))
b2=int(input("enter the breadth of the second rectangle : "))
ob=rec(l2,b2)
print("area : ",ob.area())
ob.per()
obj.comp(ob)