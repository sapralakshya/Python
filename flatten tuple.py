t1=([2,3,4,5,6],[2,4,6],[6],[5])
t2=[]
for i in t1:
    for j in i:
        t2.append(j)
print(tuple(t2))


