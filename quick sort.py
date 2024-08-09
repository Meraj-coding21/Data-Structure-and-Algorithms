import random

def func(nums, low, high):
    pivot = nums[low]
    i = low 
    j = high

    while i <= j:
        while i<=j and pivot>=nums[i]:
            i += 1
        
        while i<=j and pivot<nums[j]:
            j -= 1

        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    nums[low], nums[j] = nums[j], nums[low]
    return j

def quicksort(nums, low, high):
    if low < high:
        partition = func(nums, low, high)
        quicksort(nums, low, partition-1)
        quicksort(nums, partition + 1, high)

    return nums

nums = [random.randint(1, 100) for _ in range(1000)]

low = 0
high = len(nums) - 1

nums = quicksort(nums, low, high)

print(nums)



