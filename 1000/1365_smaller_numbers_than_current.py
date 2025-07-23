class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:
            result.append(len(list(filter(lambda x: x < i, nums))))
        return result
