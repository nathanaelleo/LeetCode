class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        wordlength = len(word)

        for i in strs[1:]:
            while word != i[0:wordlength]:
                wordlength -= 1
                if wordlength == 0:
                    return ""

                word = word[0:wordlength]

        return word   