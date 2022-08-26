ans=[]
def combSum3(arr, index, tempAns, tempSum, target, size):    
    if tempSum == target and len(tempAns) == size:
        ans.append(tempAns)
        return
    if tempSum > target:
        return
    if index == len(arr):
        return    
    
    # take 
    combSum3(arr, index + 1, tempAns+str(arr[index]), tempSum+arr[index], target, size)
    
    # not take
    combSum3(arr, index + 1, tempAns, tempSum, target, size)

arr=list(range(0,50))
n = 3

combSum3(arr, 0, '', 0, 24, n)
print(ans)