
a = list(map(int,input("Enter the elements of the list:  ").split()))
def bubblesort(a):

    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j] , a[j+1] = a[j+1] , a[j]
            
bubblesort(a)
print(a)