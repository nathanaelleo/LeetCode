class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if time < n:
            return time + 1
        elif time == n:
            return n - 1
        else:
            iterations = int(time // (n - 1))
            if iterations % 2 != 0:
                return (n - time % (n - 1))
            else:
                return (time % (n - 1) + 1)
                
#(time % n) + (iterations * 1) + 1
# n - (time % n) - 1