class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        temp = []
        diff = n-k
        num = n

        for i in range(diff,n):
            temp.append(nums[i])

        i=0

        for i in range(i,diff):
            nums[num-1] = nums[diff-1]
            num-=1
            diff-=1

        j = 0

        for i in range(k):
            nums[i] = temp[j]
            j+=1

