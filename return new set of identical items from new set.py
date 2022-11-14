set1={30,40,50,60,70}
set2={40,50,60,70,80}
set3=set()
for i in set2:
    if i in set1:
        set3.add(i)
print(set3)

