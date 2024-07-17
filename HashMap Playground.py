def twoSum(nums: list[int], target: int) -> list[int]:
        dic = {

        } #index:val
        
        dic2 = {} #index:val
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff not in dic:
                dic[i] = n
            else:
                keys = list(dic.keys())
                values = list(dic.values())
        print(keys,values)
        print(i)
        print(n)

        for j, m in enumerate(nums):
            diff = target - m
            if diff not in dic2:
                dic2[m] = j
            else:
                keys = list(dic2.keys())
                values = list(dic2.values())
        print(keys,values)
        print(j)
        print(m)



twoSum([1,2,3,4,5,5,6,100],5)