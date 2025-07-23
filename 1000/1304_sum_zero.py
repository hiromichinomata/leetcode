class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(i -  n//2)
        if n%2 == 0:
            for i in range(n//2, n):
                result[i] += 1
        return result
