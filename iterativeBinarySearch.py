#1) Write Binary Search using recursion

x = int(input("Enter the element to be searched: "))
n = int(input("Enter the number elements: "))
arr = []
for i in range(n):
    ele = int(input("Enter the element:  "))
    arr.append(ele)
    arr.sort()


def binary_search(x,arr):

    low = 0 
    high = len(arr) - 1 
    while low <= high:
        mid = (low + high) // 2
        # j = mid
        if arr[mid] == x:
            return mid

        elif arr[mid] > x: 
                high = mid - 1

        elif arr[mid] < x:
                low = mid + 1
    return -1


print(binary_search(x,arr))