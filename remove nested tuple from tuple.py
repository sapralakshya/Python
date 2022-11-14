t1=(1,4,5,(6,10),8,9)
t2=[]
for i in t1:
    if type(i) is not tuple:
        t2.append(i)
print(tuple(t2))

