set1={2,4,5,1,3,0,-1}
temp=-32768
for i in set1:
    if i>temp:
        temp=i
print("The max value is: ",temp)
temp=32767
for i in set1:
    if i<temp:
        temp=i
print("The min value is: ",temp)