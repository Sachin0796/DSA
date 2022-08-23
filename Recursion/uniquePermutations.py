tempAns=[]
def uniquePermutations(arr, index):
    if index==len(arr):
        return tempAns.append(arr.copy())             
    for i in range(len(arr)):
        arr[i] ,arr[index] = arr[index], arr[i]
        if arr not in tempAns:
            uniquePermutations(arr, index+1)
        arr[i] ,arr[index] = arr[index], arr[i]    
    return
# uniquePermutations(['1', '2', '3'],0)
uniquePermutations(['1', '1', '1'],0)
print(tempAns)