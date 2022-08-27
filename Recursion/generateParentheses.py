ans = []
def generateParenthesis(tempAns, n):
    if len(tempAns) == n*2:
        # if tempAns not in ans:
        ans.append(tempAns)
        return

    if tempAns.count('{') < n:
        generateParenthesis(tempAns+'{', n)
    if tempAns.count('}') < tempAns.count('{'):
        generateParenthesis(tempAns+'}', n)

generateParenthesis('',3)
print(ans)