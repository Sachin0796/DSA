ans=[]
def permutations1(arr, index):
    if index == len(arr):
        ans.append(arr.copy())
        return 

    for i in range(index, len(arr)):
        arr[index], arr[i] = arr[i], arr[index]
        permutations1(arr, index+1)
        arr[index], arr[i] = arr[i], arr[index]

permutations1(['a', 'b', 'c'], 0)
print(ans)