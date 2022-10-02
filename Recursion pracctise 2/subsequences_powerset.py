ans = []
def subset(arr, tempAns, index):
    
    if index == len(arr):
        ans.append(tempAns)
        return 

    #take
    subset(arr, tempAns + arr[index], index+1)
    #not take
    subset(arr, tempAns, index+1)

subset('abc', '', 0)
print(ans)