ans = []
def uniqPerm(arr, index):

    if index == len(arr):
        if arr not in ans:
            ans.append(arr.copy())
        return 
    for i in range(index, len(arr)):
        arr[i], arr[index] = arr[index], arr[i]
        uniqPerm(arr, index + 1)
        arr[i], arr[index] = arr[index], arr[i]

uniqPerm([1,1,3],0)    
print(ans)