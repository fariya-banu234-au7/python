
a = [2,4,5,677,88,1]
n = len(a)
for i in range(0,n):
    min = i
    for j in range(i+1,n):
        if a[min] > a[j]:
            min = j
        
    [a[i], a[min]] = [a[min],a[i]]
    print(a[0],a[5])
    
print(a)




















