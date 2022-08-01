def subsetSum(arr, target, index, tempAns):
    if tempAns==target:
        return True
    if index>=len(arr):
        return False
    if tempAns>target:
        return False
    #take
    a=subsetSum(arr, target, index+1, tempAns+arr[index])
    #not take
    b=subsetSum(arr, target, index+1, tempAns)    
    return a or b

print( subsetSum( [3,34,4,12,5,2], 9, 0, 0) )

