#LINEAR SEARCH


a = list(map(int,input().split()))
target = int(input("Enter the target element:  "))

def linearSearch(a,target):
    for i in range(len(a)):
        if a[i] == target:
            return i
    return -1

print(linearSearch(a,target))





        