class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        zeros = []
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                zeros.append(0)
            else:
                i += 1
        nums += zeros
