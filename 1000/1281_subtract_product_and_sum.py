class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pn = list(str(n))
        p = 1
        for i in pn:
            p *= int(i)
        s = 0
        for i in pn:
            s += int(i)
        return p-s
