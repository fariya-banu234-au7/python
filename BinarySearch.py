#Iterative!!

a = list(map(int,input().split()))
target = int(input())
a.sort()
print(a)
def binarysearch(a,target):
    low = 0
    high = len(a)-1
    
    
    while low <= high:
        mid = (low+high)//2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            low = mid + 1
        elif a[mid] > target:
            high = mid - 1
    return -1

print(binarysearch(a,target)) 


#Recursive!!

a = list(map(int,input().split()))
target = int(input())
a.sort()
print(a)
low = 0
high = len(a) - 1
def binarysearch(a,target,low,high):

    if low > high:
        return "Element not found"
        
    else:
        mid = (low + high)//2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            return binarysearch(a,target,mid+1,high)
        elif a[mid] > target:
            return binarysearch(a,target,low,mid-1)
    return -1

print(binarysearch(a,target,low,high))
