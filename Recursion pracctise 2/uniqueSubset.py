ans=[]
def uniqueSubset(arr, index, tempAns):
    if index == len(arr):
        if tempAns not in ans:
            ans.append(tempAns)
        return

    #take
    uniqueSubset(arr, index+1, tempAns+arr[index])
    #not take
    uniqueSubset(arr, index+1, tempAns)

uniqueSubset('aac', 0, '')
print(ans)