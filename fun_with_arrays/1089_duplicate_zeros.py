class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        count = 0
        old_arr = arr.copy()
        for i in old_arr:
            count += 1
            if i == 0:
                arr.insert(count, 0)
                arr.pop()
                count += 1
