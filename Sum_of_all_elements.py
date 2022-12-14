# sum of all elements of list
arr=[]
count=0
n=int(input("enter the no of elements:" ))
for k in range(0,n):
    ele=int(input())
    arr.append(ele)
print(arr)
i=int(input())
j=int(input())
for k in range(i,j+1):
    count+=arr[k]
print(count)

inp_string= input("enter the input string:")
sorted_string= inp_string.split(",")
sorted_string.sort()
print((',').join(sorted_string))
