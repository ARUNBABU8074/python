def leng(c):
    s=c.split(" ")
    l=len(s)
    l1 = len(s[0])
    l2 = len(s[1])
    if l1 > l2:
        lar = l1
        st = s[0]
    else:
        lar = l2
        st = s[1]
    for i in range(2,l-1):
        l3=len(s[i])
        if l3>lar:
            lar=l3
            st=s[i]
    print("the longest string is : ",st)
    print("its length is : ",lar)
c=input("enter the two strings : ")
leng(c)