from decimal import *

class Solution:
    def reverse(self, x: int) -> int:
        res = Decimal(str(abs(x))[::-1])
        if x < 0:
            res *= -1
        if -1*Decimal(2)**31 > res or Decimal(2)**31-1 < res:
            res = 0
        return res
