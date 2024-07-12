class Solution:
    def maxDepth(self, s: str) -> int:
        maxlist = []
        k = 1
        #find first occurance of "("
        if "(" not in s:
            return 0
        else:
            for i in range(len(s)):
                if s[i] == "(":
                    k = k + 1
                elif s[i] == ")":
                    k = k - 1
                    maxlist.append(k)
            return(max(maxlist))


#    def maxDepth(s: str):
#            
#            maxlist = []
#            k = 1
#            #find first occurance of "("
#            for i in range(len(s)):
#                if s[i] == "(":
#                    k = k + 1
#                elif s[i] == ")":
#                    k = k - 1
#                    maxlist.append(k)
#
#
#            print(maxlist)
                        
            
    maxDepth("(1+(2*3)+((8)/4))+1")
    maxDepth("(1)+((2))+(((3)))")
    maxDepth("()(())((()()))")


