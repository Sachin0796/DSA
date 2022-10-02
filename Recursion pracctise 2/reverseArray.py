def reverseArr(arr, start, end):
    if start >= end:
        return arr
    
    arr[start], arr[end] =  arr[end], arr[start]
    return reverseArr(arr, start+1, end-1)

a = [1,2,3,4,5,6]
print(reverseArr(a,0,len(a)-1))
