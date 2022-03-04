start =int(input("enter start year"))
end =int(input("enter final year"))
print("leap years:")
for year in range(start,end):
   if(year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print(year)