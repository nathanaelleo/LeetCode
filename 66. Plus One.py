class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        number = ""
        result = []

        for i in digits:
            number = number + str(i)
        
        ans = int(number) + 1

        for j in str(ans):
            result.append(int(j))
        
        return result