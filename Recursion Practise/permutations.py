ans = []
def perm(arr, index):

    if index == len(arr):
        ans.append(arr.copy())
        return
    
    for i in range(index, len(arr)):
        arr[i], arr[index] = arr[index], arr[i]
        perm(arr, index + 1)
        arr[i], arr[index] = arr[index], arr[i]

perm([1, 2, 3], 0)
print(ans)