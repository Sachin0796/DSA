def subsetSum(arr, target, index, tempTarget):

    if index == len(arr):
        return False
    
    if tempTarget == target:
        return True

    if tempTarget > target:
        return False

    a = subsetSum(arr, target, index + 1, tempTarget + arr[index])
    b = subsetSum(arr, target, index + 1, tempTarget)

    return a or b

print(subsetSum( [3,34,4,12,10,2], 20, 0, 0) )