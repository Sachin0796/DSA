ans=[]
def combSum(arr, index, tempAns, target, tempSum):
    if tempSum == target:
        if tempAns not in ans:
            ans.append(tempAns)
        return
    if tempSum>target:
        return
    if index >= len(arr):
        return
    #take
    combSum(arr, index, tempAns+str(arr[index]), target, tempSum+arr[index])
    #not take
    combSum(arr, index+1, tempAns, target, tempSum)
        
arr=[3,12,9,11,6,7,8,5,4,3]
arr.sort()
combSum(arr,0, '', 15, 0)
print(ans)

