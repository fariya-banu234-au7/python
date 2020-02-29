def mergeSort(arr,i,j):
    if(i != j):
        mid = (i+j)//2
        mergeSort(arr,i,mid)
        mergeSort(arr,mid,j)
        merge(arr,i,j)

def merge(i,mid,j):
    i = arr[:mid]
    j = arr[mid:]
    m = n = k = 0
    b = []
    while m < len(i) and n < len(j):
        if i[m] > j[n]:
            b[k] = j[n]
            n += 1
        else:
            b[k] = i[m]
            m += 1
        k += 1

    if m < len(i):
        b.append(i[m:])
    elif n < len(j):
        b.append(j[n:])

    return b

arr = [2,4,5,6,7,12,78,9]
print(arr)
mergeSort(arr,i,j)
print(arr)

            
               

