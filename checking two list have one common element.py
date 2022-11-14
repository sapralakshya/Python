list1=[1,2,3,11,12]
list2=[4,5,6,7,8]
for i in list1:
    if i in list2:
        print(True)
        break
else:
    print(False)

