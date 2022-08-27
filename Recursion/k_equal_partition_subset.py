def kEqualPart(arr, index, tempAns, tempTarget, tempSum, visitedValues):
    if len(ans) == k and True not in visitedValues:
        return
    if tempSum == tempTarget:
        kEqualPart(arr, 0, '', tempTarget, 0, visitedValues)        
        ans.append(tempAns)
        return
    if tempSum > tempTarget:
        return
    if index == len(arr):        
        return
    if visitedValues[index] == True:
        kEqualPart(arr, index+1, tempAns, tempTarget, tempSum, visitedValues)         
        return
    else:
        # take
        visitedValues[index] = True
        kEqualPart(arr, index+1, tempAns + str(arr[index]), tempTarget, tempSum+arr[index], visitedValues)
        #not take        
        visitedValues[index] = False
        kEqualPart(arr, index+1, tempAns, tempTarget, tempSum, visitedValues)       
        return

arr=[1,1,1,1,2,2,2,2]
k = 4
visitedValues = [False] * len(arr)
ans=[]
sum1 = sum(arr)
tempTarget = 0
if sum1 % k != 0:
    print("Subsets cannot be formed!")
else:
    tempTarget = sum1/k
    kEqualPart(arr, 0, '', tempTarget, 0, visitedValues)
    if len(ans) >= k:
        print(ans)
    else:
        print("Subsets formed but not K")
        print(ans)