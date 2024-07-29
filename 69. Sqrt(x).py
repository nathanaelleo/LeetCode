class Solution:
    def mySqrt(self, x: int) -> int:
        
        i = 0
        while True:
            if i * i <= x:
                i = i + 1
            else:
                return i - 1

