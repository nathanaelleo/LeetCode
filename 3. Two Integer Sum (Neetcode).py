class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)-1):
            for j in range(len(nums)-1-i):
                j = j + i + 1
                s1 = nums[i]
                s2 = nums[j]
                if s1 + s2 == target:
                    return[i,j]
