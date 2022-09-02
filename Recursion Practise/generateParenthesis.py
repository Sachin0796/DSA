ans = []
def generateParenthesis(n, tempAns, opening, closing):    

    if len(tempAns) == 2*n:
        ans.append(tempAns)
        return

    if opening < n:
        generateParenthesis(n, tempAns + '{', opening + 1, closing)
    if closing < opening:
        generateParenthesis(n, tempAns + '}', opening, closing + 1)

generateParenthesis(3, '', 0, 0)
print(ans)