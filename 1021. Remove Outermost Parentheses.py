class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        indicator = 0
        #if fulfils objective, collect
        collection = []
        strings = ""
        #condition, when it is open, collect
        for i in range(len(s)):
            if s[i] == "(":
                indicator = indicator + 1
            if s[i] == ")":
                indicator = indicator - 1
            if indicator != 1 and s[i] == "(":
                collection.append(s[i])  
            if indicator != 0 and s[i] == ")":
                collection.append(s[i])
        return(strings.join(collection))



def removeOuterParentheses(s: str):
        #create a variable to indicate if the parentheses is open or closed
        #1 means open 0 means closed
        indicator = 0
        #if fulfils objective, collect
        collection = []
        strings = ""
        #condition, when it is open, collect
        for i in range(len(s)):
            if s[i] == "(":
                indicator = indicator + 1
            if s[i] == ")":
                indicator = indicator - 1
            if indicator != 1 and s[i] == "(":
                collection.append(s[i])  
            if indicator != 0 and s[i] == ")":
                collection.append(s[i])
            
            
            #print(s[i])
            print(indicator)
         
        print(strings.join(collection))

removeOuterParentheses("(()())(())(()(()))")

"(()())(())"

"(()())(())(()(()))"
