class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return len(sorted("".join(list(map(str, nums))).split('0'), reverse=True)[0])
