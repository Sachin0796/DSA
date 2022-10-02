#for given range of numbers, find the n numbers that has sum equal to given target
ans=[]
def combsum3(arr, tempAns, tempSum, index, target, nLen,tempcount):
    if tempSum == target and tempcount == nLen:
        ans.append(tempAns)
        return
    if tempSum>target:
        return    
    if index == len(arr):
        return
    #take
    combsum3(arr, tempAns+str(arr[index]), tempSum+arr[index], index+1, target, nLen,tempcount+1)
    #not take
    combsum3(arr, tempAns, tempSum, index+1, target, nLen, tempcount)

a = range(1,51)
combsum3(a, '', 0, 0, 24, 3, 0)
print(ans)