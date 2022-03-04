list1 = [ "ARUN" , "BABU" ]
res = [ord (ele) for sub in list1 for ele in sub]
print(res)