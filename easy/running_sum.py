class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        count = 0
        result = []
        for i in range(len(nums)):
            count += nums[i]
            result.append(count)
        return result
