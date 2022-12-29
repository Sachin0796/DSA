ans=[]
def coinsCount(arr, index, tempAns, target, tempSum):
    if index == len(arr):
        if tempSum==target:
            ans.append(tempAns)
        return

    if tempSum==target:
        ans.append(tempAns)
        return
    
    if tempSum>target:
        return
    
    # take
    coinsCount(arr, index, tempAns+str(arr[index]), target, tempSum+arr[index])
    #not take
    coinsCount(arr, index+1, tempAns, target, tempSum)

arr=[1,2,5]
coinsCount(arr, 0, '', 20, 0)
print(ans)