class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        i = 0
        old = -100000000000
        old_nums = nums.copy
        for _ in range(size):
            val = nums[i]
            if old == val:
                nums.pop(i)
            else:
                i += 1
                old = val
        return len(nums)
