class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_nums = list(filter(lambda x: x!= val, nums))
        for _ in range(len(nums)):
            nums.pop()
        for i in new_nums:
            nums.append(i)
        return len(nums)
