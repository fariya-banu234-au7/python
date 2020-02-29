
n = int(input("Enter range: "))
a = []
for i in range(n):
    ele = int(input("Enter element: "))
    a.append(ele)
    a.sort()
# a = sorted(a)
print(a)
# a = [2,4,5,7,8,12,14,25,36,48,50]
low = 0
high = len(a) - 1
x = int(input("Enter the element to be searched:  "))



def bsearch(a,x,low,high):
    if low > high:
        return "Element not found"
    
    else:
        mid = (low + high)//2
        if a[mid] == x:
            return mid
        elif a[mid] > x:
            return bsearch(a,x,low,mid-1)     
        elif a[mid] < x:
            return bsearch(a,x,mid+1,high)     

print(bsearch(a,x,low,high))



# n = int(input("Enter range: "))
# a = []
# for i in range(n):
#     ele = int(input("Enter element: "))
#     a.append(ele)
#     # a.sort()  ------  remove this line
# a = sorted(a)  #  Add this line
# print(a)
# low = 0
# high = n - 1
# x=4
# # mid = (low + high)//2
# def bsearch(a,x,low,high):
#     if low > high:
#         return "Element not found"
#     else:
#         mid = (low + high)//2
#         if a[mid] == x:
#             return mid
#         elif a[mid] > x:
#             return bsearch(a,x,low,mid-1)     
#         elif a[mid] < x:
#             return bsearch(a,x,mid+1,high) 
#         else:
#             return "Element not found"    
# print(bsearch(a,x,low,high))