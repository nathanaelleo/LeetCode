class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        operation = 0
        for num in nums:
            operation ^= num

        return operation