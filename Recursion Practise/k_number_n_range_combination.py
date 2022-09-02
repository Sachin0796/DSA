ans = []
def nSizeSubset(arr, index, tempAns, n):

    if index == len(arr):
        if len(tempAns) == n:
            ans.append(tempAns)
        return
    
    #take
    nSizeSubset(arr, index + 1, tempAns + arr[index], n)
    # not take
    nSizeSubset(arr, index + 1, tempAns, n)

nSizeSubset(['1','2','3','4'], 0, '', 3)
print(ans)