dict={'b':[4,2],'c':[8,6],'a':[10,5]}
dict1={}
for i in sorted(dict):
    dict1[i]=None
for i in dict:
    for j in dict[i]:
        dict1[i]=sorted(dict[i])
print(dict1)
