#incomplete!
def removeOuterParentheses(s: str):
        #create a variable to indicate if the parentheses is open or closed
        #1 means open 0 means closed
        indicator = 0
        score = 0
        #if fulfils objective, collect
        collection = []
        collectionv2 = []
        collectionv3 = []
        #condition, when it is open, collect
        for i in range(len(s)):
            if s[i] == "(":
                indicator = indicator + 1
                collectionv2.append(indicator)
            if s[i] == ")":
                indicator = indicator - 1
                collectionv2.append(indicator)
            if indicator == 0:
                for j in range(len(collectionv2)):
                    if collectionv2[j] > collectionv2[j - 1] and collectionv2[j] > collectionv2[j + 1]:
                        collection.append(collectionv2[j])
                
                maxvalv1 = max(collection)
                print(collection)

                k = 0
                while max(collection) != min(collection):
                    maxval = max(collection)
                    if collection[k] == maxval:
                        score = score + 1
                        collection.pop(k)
                        k = 0 
                    else:
                        k = k + 1
                    if maxvalv1 != maxval:
                        score = score * 2
                print(collection)
                print(score)
                maxval = max(collection)
                

                if max(collection) == min(collection):
                    score = len(collection) * 2 ** (maxval-1) + score
                collectionv2.clear()
                collection.clear()
                collectionv3.append(score)
                score = 0
            
        print(sum(collectionv3))

        #print(strings.join(collection))
removeOuterParentheses("()(())()(((()(()())))(((())(()))()))(((())))")
#removeOuterParentheses("((()()))")
#removeOuterParentheses("(()(()))")
#removeOuterParentheses("()()")
#removeOuterParentheses("(()())(())(()(()))")
#4 + 2 + (3) * 2 