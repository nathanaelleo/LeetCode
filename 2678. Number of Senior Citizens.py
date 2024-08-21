class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(1 if int(i[11:13])>60 else 0 for i in details)