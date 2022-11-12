value="Python is great and java is also great"
res=value.split(" ")
res1=[]
for i in range(0,len(res)):
    for j in range(i+1,len(res)):
        if res[i] == res[j]:
            res1.append(res[j])
print(res1)
for i in res1:
    res.remove(i)
for i in res:
    print(i,end=" ")