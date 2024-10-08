class Solution:
    def romanToInt(self, s: str) -> int:
        #d for dictionary
        d = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        total = 0

        if len(s) == 1:
            total = d[s[0]]
            return total

        for i in range(len(s)-1):
            if d[s[i]] < d[s[i+1]]:
                total = total - d[s[i]]
            else: 
                total = total + d[s[i]]

        return total + d[s[-1]]

