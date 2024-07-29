class Solution:
    def mySqrt(self, x: int) -> int:
        
        i = 0
        while True:
            if i * i <= x:
                i = i + 1
            else:
                return i - 1


class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid -1
            else:
                return mid
            
        return right