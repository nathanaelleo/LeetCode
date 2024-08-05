class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        map = {}
        j = 0

        for i in arr:
            if i not in map:
                map[i] = True
            else:
                map[i] = False
        
        for i in arr:
            if map[i]:
                j += 1
                if j == k:
                    return i

        return ""
                