
def Selectionsort(a):
    for i in range(len(a)):
        minimum = i
        for j in range(i+1,len(a)):
            if a[j] < a[minimum]:
                minimum = j

        a[i],a[minimum] = a[minimum],a[i]


a = list(map(int,input().split()))
Selectionsort(a)
print(a)


