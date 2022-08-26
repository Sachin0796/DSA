ans=[]
def wordsFromDigit(arr, tempAns, index):
    if len(arr) == index:
        ans.append(tempAns)
        return
    for i in range(len(arr[index])):
        wordsFromDigit(arr, tempAns+arr[index][i], index+1)