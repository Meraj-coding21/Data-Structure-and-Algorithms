import random

def search(arr,n,target):
    low= 0
    high= n-1

    while low<=high:

        mid= (low + high) // 2

        if arr[mid] == target:
            return mid
        
        elif target > arr[mid]:
            low= mid + 1
        
        else:
            high= mid - 1

    return -1


arr=[random.randint(1,100) for _ in range(100)]

print(arr)
arr.sort()
print(arr)

target= int(input())

index= search(arr,len(arr),target)
print(index)