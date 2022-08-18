# find all the possible permutations of a given array
# Need to check why append is not working properly
tempAns=[]
def permutations1(arr, index):    
    if index==len(arr):                                                
        tempAns.append(arr.copy())        
        return    
    for i in range(index,len(arr)):
        arr[i],arr[index]=arr[index],arr[i]    
        permutations1(arr, index+1)
        arr[i],arr[index]=arr[index],arr[i]
    return

permutations1([1,2,3],0)
print(tempAns)

# in built code
# from itertools import permutations
# for i in permutations(list('123')):
#     print(i)