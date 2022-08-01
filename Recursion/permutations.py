# # find all the possible permutations of a given array

def permutations(arr, index, tempAns):
    if index==len(arr):
        return tempAns

    for i in range(index,len(arr)):
        arr[i], arr[index]=arr[index], arr[i]        
        tempAns+=permutations(arr, index+1,tempAns)
        arr[i], arr[index]=arr[index], arr[i]
        return tempAns

print(permutations(['123'],0,''))