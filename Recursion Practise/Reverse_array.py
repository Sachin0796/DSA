def reverseArray(arr, first, last):
    
    if first >= last:
        return arr
    
    arr[first], arr[last] =  arr[last], arr[first]
    return reverseArray(arr, first + 1, last - 1)

arr=[1,2,3,1]

print(reverseArray(arr, 0, len(arr) - 1))