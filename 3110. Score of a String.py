class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        for i in range(len(s)-1):
            total = total + abs(ord(s[i]) - ord(s[i+1]))
        return total
    
#O(N) 37ms 51.1%