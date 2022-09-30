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
    if str(arr[index]) not in tempAns:
        combSum(arr, index + 1, tempAns+str(arr[index]), target, tempSum+arr[index])
    #not take
    combSum(arr, index + 1, tempAns, target, tempSum)
        
arr=[4,7,8]
arr.sort()
combSum(arr,0, '', 15, 0)
print(ans)

