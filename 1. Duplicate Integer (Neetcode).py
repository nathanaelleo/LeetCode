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
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = nums[i]
            else:
                return True
        return False