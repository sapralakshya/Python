arr=[]
count=0
n=int(input("enter the no of elements:" ))
for i in range(0,n):
    ele=int(input())
    arr.append(ele)
print(arr)
for i in arr:
    count+=i
print(count)