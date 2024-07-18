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
        print(i) #index
        print(n) #value

        #j is the pointer, 0,1,2
        #m is the value 1,2,3,4
        for j, m in enumerate(nums):
            diff2 = target - m
            if diff2 not in dic2:
                dic2[m] = j
            else:
                keys = list(dic2.keys())
                values = list(dic2.values())
        print(keys,values)
        print(j) #value
        print(m) #index



twoSum([1,2,3,4,5,5,6,100],5)