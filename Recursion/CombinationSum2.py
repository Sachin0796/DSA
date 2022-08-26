ans=[]
def combSum2(arr, index, tempAns, target, tempSum):
    if tempSum==target:    
        if tempAns not in ans:            
            ans.append(tempAns)
        return
    if tempSum>target:
        return
    if index >= len(arr):
        return
    #take
    if str(arr[index]) not in tempAns:
        combSum2(arr, index+1, tempAns+str(arr[index]), target, tempSum+arr[index])
    #not take
    combSum2(arr, index+1, tempAns, target, tempSum)
        
arr=[3,3,3,3,12,9,11,6,7,8,5,4]
arr.sort()
combSum2(arr,0, '', 15, 0)
print(ans)

