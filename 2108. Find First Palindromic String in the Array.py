
def firstPalindrome(words: list[str]) -> str:
    
    for word in words:
        isPalindrome = True
        num = len(word)
        i = 0
        for i in range((num//2) + 1):
            if word[i] != word[num-i-1]:
                isPalindrome = False

        if isPalindrome:
            return word

array1 = ["abc","car","racecar","cool"]

print(firstPalindrome(array1))

class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            isPalindrome = 1
            num = len(word)
            i = 0
            for i in range((num//2) + 1):
                if word[i] != word[num-i-1]:
                    isPalindrome = 0

            if isPalindrome == 1:
                return word
        return ""