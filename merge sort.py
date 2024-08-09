def mergesort(arr,l,r):

    if l>=r:
        return
    else:
        m= (l+r)//2

        mergesort(arr,l,m)
        mergesort(arr,m+1,r)
        merge(arr,l,m,r)

def merge(arr,l,m,r):
    left=l
    right=m+1
    temp=[]

    while(left<=m and right<=r):
        if(arr[left]<=arr[right]):
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1

    while(left<=m):
        temp.append(arr[left])
        left+=1

    while(right<=r):
        temp.append(arr[right])
        right+=1

    for i in range(l,r+1):
        arr[i]= temp[i-l]


arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
mergesort(arr, 0, n - 1)
print("Sorted array is:", arr)


