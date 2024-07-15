class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        lengthx = len(strx)
        for i in range(lengthx -1):
            if strx[i] != strx[lengthx - i - 1]: 
                return False
        return True



def isPalindrome(self, x: int) -> bool:
    #divide by 10 and modulus 10 to get the last number

    if x < 0:
        return False
    
    reverse = 0
    xcopy = x

    while x > 0:
        reverse = (reverse * 10) + (x % 10)
        x = x / 10
        
    return xcopy == reverse
