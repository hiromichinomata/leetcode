class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        new_heights = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != new_heights[i]:
                count += 1
        return count
