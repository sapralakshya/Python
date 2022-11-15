def count_digits(t1):
    return sum([len(str(ele)) for ele in t1])
t1=[(3,4,6,723),(1,2),(234,243,55)]
t1.sort(key=count_digits)
print(t1)