import random

def func(arr, low, high, target):
    if(low>high):
        return -1
    
    mid= (low + high)//2

    if arr[mid] == target:
        return mid
    
    elif target > arr[mid]:
        return func(arr, mid+1, high, target)
    
    else:
        return func(arr, low, mid-1, target)
    
def search(arr, n, target):

    return func(arr, 0, n-1, target)

arr=[random.randint(1,100) for _ in range(100)]

print(arr)
arr.sort()
print(arr)

target= int(input())

index= search(arr,len(arr),target)
print(index)