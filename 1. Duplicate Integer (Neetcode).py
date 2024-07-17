def hasDuplicate(nums: list[int]) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = nums[i]
            else:
                print("True")
        print("False")

hasDuplicate([1,2,3,4,5,5])


#Neetcode Solution:
#V1 Solution
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = nums[i]
            else:
                return True
        return False
    
#V2 Solution
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic = {} #index:val
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dic:
                return [dic[diff], i]
            dic[n] = i
        return           