list1=[2,[3,4,5],[3,4,5],[4,5],[6,7]]
list2=[]
for j in list1:
    if type(j) is list:
      for i in j:
        list2.append(i)
    else:
        list2.append(j)
print(list2)