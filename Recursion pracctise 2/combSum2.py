ans=[]
def combSum(arr, tempAns, tempSum, index, target):
    
    if tempSum == target:
        ans.append(tempAns)
        return
    if tempSum>target:
        return    
    if index == len(arr):
        return
    #take
    combSum(arr, tempAns+str(arr[index]), tempSum+arr[index], index+1, target)
    #not take
    combSum(arr, tempAns, tempSum, index+1, target)
a = [1,2,3,4,5]
combSum(a, '', 0, 0, 5)
print(ans)