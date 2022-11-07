# Finding the triplet in a list whose sum is equal to input value
list1=[12,3,9,4,1,2]
triplet_sum=24
list2=[]
for i in range(0,len(list1)):
    for j in range (i+1,len(list1)):
        for k in range (j+1,len(list1)):
            if (list1[i]+list1[j]+list1[k]==triplet_sum):
                list2.append(list1[i])
                list2.append(list1[j])
                list2.append(list1[k])
print(list2)
