#incomplete!
def removeOuterParentheses(s: str):
        #create a variable to indicate if the parentheses is open or closed
        #1 means open 0 means closed
        indicator = 0
        score = 0
        #if fulfils objective, collect
        collection = []
        collectionv2 = []
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
                maxval = max(collection)



                while len(collection) > 1:
                    for k in collection:
                        if k == maxval:
                            score = score + 1
                            collection.pop()

                print(maxval)        
                print(collection)
                print(score)
                #    maxval = max(collection)
                #score = score * 2
                #collectionv2.clear()
                #collection.clear()
        
                        

                
                

            #print(indicator)
            #print(score)
            #print(s[i])
            #print(collection)
            #print(score)
            #print(s[i])
        #print(collection)
         
        #print(strings.join(collection))
#removeOuterParentheses("((()()))")
removeOuterParentheses("(()(()))")
#removeOuterParentheses("()()")
#removeOuterParentheses("(()())(())(()(()))")
#4 + 2 + (3) * 2 