from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_counts = defaultdict(int)
        for char in s:
            char_counts[char] += 1
        for i in range(len(s)):
            if char_counts[s[i]] == 1:
                return i
        return -1
