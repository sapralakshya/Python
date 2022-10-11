
arr=[1,2,3,4,5,6,7]
lst = []
d=int(input("Enter the positions to be skipped "))
i=0
while (i<d):
    lst.append(arr[i])
    i=i+1
for k in range(0,len(arr)):
    if k+d<len(arr):
      arr[k]=arr[k+d]
for k in range(-1,-(d+1),-1):
    arr[k]=lst[k]
print(arr)