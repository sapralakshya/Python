# Finding second most freq element
lst=["aaa","aaa","aaa","bbb","bbb","ccc"]
num=lst[0]
temp=0
for i in lst:
    temp=max(temp,lst.count(i))
    if(lst.count(i)==temp):
        num=i
for i in range(0,temp):
    lst.remove(num)
temp=0
num=lst[0]
for i in lst:
    temp=max(temp,lst.count(i))
    if(lst.count(i)==temp):
        num=i
print(num)
