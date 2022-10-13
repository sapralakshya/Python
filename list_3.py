list1=[10,15,20,25,30,35,40]
list2=[25,40,35]
list3=[]
for i in list1:
    if i not in list2:
        list3.append(i)
print(list3)