a = [5,2,4,7,9,1,3,5,4,0,6,1,3]
for i in range(len(a)):
    for j in range(len(a)-1):
        tmp = 0
        if a[j] > a[j+1]:
            tmp = a[j]
            a[j] = a[j+1]
            a[j+1] = tmp
print(a)

