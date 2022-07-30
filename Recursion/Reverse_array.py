def reverseArray(arr, start, end):
    if start>=end:
        return arr
    arr[start],arr[end]=arr[end],arr[start]
    reverseArray(arr,start+1,end-1)
    return arr

arr=[6,8,3,4,9,10]
print(reverseArray(arr,0,len(arr)-1))