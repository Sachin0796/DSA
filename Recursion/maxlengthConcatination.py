ans=[0]
ans[0] = 0
def maxLength(arr, tempAns, index):
            
    if index == len(arr):
        if len(tempAns) == len(set(tempAns)) and len(tempAns) > ans[0]:            
            ans[0] = len(tempAns)        
        ans.append(tempAns)
        return
    
    #take
    maxLength(arr, tempAns+arr[index], index + 1)

    # not take
    maxLength(arr, tempAns, index + 1)
maxLength(['cha','r','act','ers'], '', 0)
print(ans[0])
print(ans)