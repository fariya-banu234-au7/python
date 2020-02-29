
a = list(map(int,input().split()))

count = [0] * (max(a) + 1)

#for storing each element:
for i in range(len(a)-1):
    count[a[i]] += 1

#for cum sum:
for j in range(0,len(a)):
    count[j] = count[j] + count[j-1]

b = []
#for creating a new array to store as per count:
for k in range(len(a)-1,0,-1):
    b[count[a[k]]- 1] = a[k]
    count[a[k]] = count[a[k]] - 1

#for final sorted array:
for l in range(len(a)-1):
    a[l] = b[l]



