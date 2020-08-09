from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        notes = defaultdict(int)
        for i in nums:
            notes[i] += 1
        for key, value in notes.items():
            if value != 2:
                return key
