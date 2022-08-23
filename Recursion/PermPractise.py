ans=[]
def perm(arr, index):
    if index==len(arr):
        ans.append(arr.copy())
        return
        
    for i in range(index,len(arr)):
        arr[index], arr[i] =  arr[i], arr[index]
        perm(arr, index+1)
        arr[index], arr[i] =  arr[i], arr[index]

perm([1,2,3],0)
print(ans)