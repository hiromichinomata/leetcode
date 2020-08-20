class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        m = max(A)
        s = A.index(m)
        if s == 0 or s == len(A) - 1:
            return False
        for i in range(1,s):
            if A[i] - A[i-1] <= 0:
                return False
        for i in range(s+1, len(A)):
            if A[i-1] - A[i] <= 0:
                return False
        return True
