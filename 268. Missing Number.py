class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        arithsum = (n*(n+1))/2
        vectorsum = sum(nums)
        missing_num = arithsum - vectorsum
        return int(missing_num)