t1=(1,1,0,1,0,0,1)
number=0
j=len(t1)-1
for i in t1:
    number=number+(i*pow(2,j))
    j=j-1
print(number)