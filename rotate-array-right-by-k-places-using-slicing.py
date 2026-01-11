class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        nums.reverse()                   #nums = [7,6,5,4,3,2,1]

        nums[0:k] = reversed(nums[0:k])  #nums = [5,6,7,4,3,2,1]

        nums[k:n] = reversed(nums[k:n])  #nums = [5,6,7,1,2,3,4]

        