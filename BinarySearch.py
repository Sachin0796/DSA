# trying
# 1,3,5,7, 9 ,11,"15",17,19
# 0,1,2,3, 4 ,5,6,7,8

def binarySearch(arr, start, end, mid, target):
    
    # check if value found
    if arr[mid] == target:
        return mid    
    # value not found so start will be moved ahead of end.
    if start >= end:
        return -1

    # if target is greater than mid    
    if arr[mid] < target:
        start = mid + 1

    # if target is smaller than mid    
    elif arr[mid] > target:
        end = mid - 1
    
    # recalculate  mid
    mid = (start + end) // 2
    return binarySearch(arr, start, end, mid, target)

arr = [1,3,5,7,9,11,15,17,19]
middle = (len(arr)-1)//2
index = binarySearch(arr, 0, len(arr)-1, middle, 15)
print(index)