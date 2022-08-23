ans=[]
def allSubset(arr, tempAns, index):
    if index==len(arr):
        if tempAns not in ans: 
            ans.append(tempAns)
        return    
    # take
    allSubset(arr, tempAns+arr[index], index+1)    
    # not take
    allSubset(arr, tempAns, index+1)    
allSubset(['1','2','2'],'',0)
ans.sort()
print(ans)