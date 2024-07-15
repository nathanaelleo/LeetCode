class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        lengthx = len(strx)
        for i in range(lengthx -1):
            if strx[i] != strx[lengthx - i - 1]: 
                return False
        return True

