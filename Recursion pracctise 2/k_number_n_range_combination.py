ans=[]
def nLengthCombinations(arr, index, tempAns, n):
    if index == len(arr):
        if len(tempAns) == n:
            ans.append(tempAns)
        return
    #take
    nLengthCombinations(arr, index+1, tempAns+arr[index], n)
    #not take
    nLengthCombinations(arr, index+1, tempAns, n)

nLengthCombinations('12345', 0, '', 4)
print(ans)