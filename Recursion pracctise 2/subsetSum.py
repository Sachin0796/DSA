def subsetSum(arr, index, target, tempSum):

    if tempSum == target:
        return True
    
    if index == len(arr):
        return False
    
    if tempSum>target:
        return False

    #take
    a = subsetSum(arr, index+1, target, tempSum+arr[index])
    #not take
    b = subsetSum(arr, index+1, target, tempSum)

    return a or b

print(subsetSum([3,34,4,12,10,2], 0, 15, 0))

