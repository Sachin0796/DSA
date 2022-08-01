import copy

def subArraySum1(arr, brr, target, index, tempAns, tempIndex):
    if tempAns==target:
        return tempIndex
    if index==len(arr):
        return -1
    
    subArraySum1(arr, brr, target, index+1, tempAns+arr[index], tempIndex.append(index))
    subArraySum1(arr, brr, target, index+1, tempAns, tempIndex.append(index))
    
arr=[1,2,3,7,5]
brr=copy.copy(arr)
arr.sort()
subArraySum1(arr, brr, 12, 0, 0, [])