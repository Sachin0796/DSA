ans=[]
def uniquePerm(arr, index):
    if index == len(arr):
        if arr not in ans:
            ans.append(arr.copy())
        return
    
    for i in range(index, len(arr)):
        arr[index], arr[i] = arr[i], arr[index]
        uniquePerm(arr, index+1)
        arr[index], arr[i] = arr[i], arr[index]

a= [1,1,3]
uniquePerm(a, 0)
print(ans)