def sort(a ):
    size = len(a)
    output = [0] * size
    count = [0] * 10
    for j in range(0, size):
        count[a[j]] = count[a[j]] + 1

    for j in range(0, 10):
        count[j] = count[j -1]
    
    j = size - 1
    while j >= 0:
        output[count[a[j] - 1]] = a[j]
        count[a[j]] = count[a[j]] - 1
        j = j - 1

    for j in range(0,size):
        a[j] = output[j]

list = [1, 12, 2, 4, 3, 5, 9, 12,12, 12]

sort(list)

print("The sorted array  is : ")
print(list)

    