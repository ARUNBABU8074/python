d1={"name:":"arun","age:":21}
d2={"course:":"mca","rollno:":38}
print("dictionary 1 : ",d1)
print("dictionary 2 : ",d2)
d=d1.copy()
d.update(d2)
print("merged dictionary : ",d)