class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        memo = {}
        for i in range(1, len(nums)+1):
            memo[i] = -1
        for i in nums:
            memo[i] += 1

        res = []
        for k, v in memo.items():
            if v == -1:
                res.append(k)
        return sorted(res)
