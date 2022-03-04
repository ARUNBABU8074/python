class bank:
    def __init__(self,a,n,t,b):
        self.an=a
        self.name=n
        self.tp=t
        self.bal=b
    def deposit(self,a):
        self.bal+=a
        print("available balance : ",self.bal)
    def withdraw(self,a):
        if(self.bal < a):
            print("low balance")
        else:
            self.bal-=a
            print("available balance : ",self.bal)
a=int(input("enter acnt num : "))
n=input("enter name : ")
t=input("acnt type : ")
b=int(input("enter acnt balance : "))
obj=bank(a,n,t,b)
am=int(input("enter the amount to be deposit :"))
obj.deposit(am)
aw=int(input("enter the amount to be withdraw :"))
obj.withdraw(aw)