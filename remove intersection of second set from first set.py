set1={2,3,4,5}
set2={4,5,6,7}
for i in set2:
    if i in set1:
        set1.remove(i)
print(set1)
print(set2)