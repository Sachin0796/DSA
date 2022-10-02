ans = []
def possibleWordsFromDigit(arr, index, tempAns):
    if index == len(arr):
        ans.append(tempAns)
        return 
    for i in range(len(arr[index])):
        possibleWordsFromDigit(arr, index+1, tempAns + arr[index][i])
    

myDict = {2:'abc', 3:'def', 4:'ghi'}
arr = [myDict[2], myDict[3], myDict[4]]
possibleWordsFromDigit(arr, 0, '')
print(ans)
print(len(ans))