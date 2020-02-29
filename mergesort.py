#Iterative approach!!
def mergesort(A):
    
    if len(A) < 2:
        return A
    else:
        mid = len(A)//2
        # return mergesort(A[:mid])
        # return mergesort(A[mid:])
        return merge(mergesort(A[:mid]),mergesort(A[mid:]))
           


def merge(L,R):
    # low = 0
    # high = len(A)
    # L = A[:mid]
    # R = A[mid:]
    b = []
    i = 0
    j =0 
    # k = 0
    while i < len(L) and j < len(R):
        if L[i] >= R[j]:
            b.append(R[j])
            j += 1
        else:
            b.append(L[i])
            i += 1
        # k += 1

    # while i < len(L):
    #     b[k] = L[i]
    #     i += 1
    #     k += 1

    # while j < len(R):
    #     b[k] = R[j]
    #     j += 1
    #     k += 1

    b.append(L[i:])
    b.append(R[j:])
    return b

# A = list(map(int,input().split()))
A = [3, 1, 9, 7, 2, 8]
print("Original array is :", A)
mergesort(A)
print("Array after merge sort is:")
print(A)

# #Recursive Approach!!
# def mergesort(A):
   
#     if len(A) >1:
#         mid = len(A)//2
#         L = A[:mid]
#         R = A[mid:]

#         mergesort(L)
#         mergesort(R)
        
#         i,j,k = 0,0,0

#         while i < len(L) and j < len(R):
#             if L[i] > R[j]:
#                 A[k] = R[j]
#                 j += 1
#             else:
#                 A[k] = L[i]
#                 i += 1
#             k += 1

#         while i < len(L):
#             A[k] = L[i]
#             i += 1
#             k += 1

#         while j < len(R):
#             A[k] = R[j]
#             j += 1
#             k += 1
#         return A
# A = [23,56,78,12,34,14,15,10,2,3,6]
# print("Original array is:")
# print(A)
# print("Sorted array is:")
# mergesort(A)
# print(A)