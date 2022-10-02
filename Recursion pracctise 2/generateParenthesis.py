ans=[]
def generateParenthesis(n, open, close, tempAns):
    
    if len(tempAns) == 2*n:
        ans.append(tempAns)
        return

    if open<n:
        generateParenthesis(n, open+1, close, tempAns+'{')    
    if open>close:
        generateParenthesis(n, open, close+1, tempAns+'}')    
    

generateParenthesis(3, 0, 0, '')
print(ans)

    
