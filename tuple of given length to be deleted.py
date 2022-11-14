list1=[(4,5),(4," " ),(3,4,5),(3,4)]
k=int(input("Enter the length:"))
for i in list1:
    if len(i)==k:
        list1.remove(i)
print(list1)