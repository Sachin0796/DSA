ans=[]
def combSum(arr, tempAns, tempSum, index, target):
    if tempSum == target:
        ans.append(tempAns)
        return

    if index == len(arr):
        return
    
    if tempSum>target:
        return    
    #take
    combSum(arr, tempAns+str(arr[index]), tempSum+arr[index], index, target)
    #not take
    combSum(arr, tempAns, tempSum, index+1, target)
a = [1,2,3]
combSum(a, '', 0, 0, 6)
print(ans)