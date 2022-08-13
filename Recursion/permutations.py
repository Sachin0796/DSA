# find all the possible permutations of a given array
# Need to check why append is not working properly
tempAns=[]
def permutations(arr, index):    
    if index==len(arr):                                                
        tempAns.append(arr)
        print("Here is arr:",arr) 
        return    
    for i in range(index,len(arr)):
        arr[i],arr[index]=arr[index],arr[i]        
        permutations(arr, index+1)
        arr[i],arr[index]=arr[index],arr[i]
    return

permutations([1,2,3],0)
print(tempAns)

# from itertools import permutations
# for i in permutations(list('123')):
#     print(i)