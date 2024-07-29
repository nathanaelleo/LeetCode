class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = ""

        i = 1
        while i <= len(s):
            if s[-i] != " ":
                word = word + s[-i]
            elif s[-i] == " " and word == "":
                word = word
            elif s[-i] == " " and word != "":
                break
            i = i + 1
        
        return len(word)
            
