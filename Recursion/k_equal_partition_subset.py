arr=[1,1,1,1,2,2,2,2]
k = 2
visitedValues = [False] * len(arr)
ans=[]
sum1 = sum(arr)
tempTarget = 0
def kEqualPart(arr, index, tempAns, tempTarget, tempSum):

    if len(ans) == k:
        return
    if tempSum == tempTarget:
        kEqualPart(arr, 0, '', tempTarget, 0)
        if tempAns not in ans:
            ans.append(tempAns)
        return 
          
    if tempSum > tempTarget:
        return           

    if index == len(arr):        
        return  

    if visitedValues[index] == True:
        kEqualPart(arr, index+1, tempAns, tempTarget, tempSum)
        return

    else:
        # take
        visitedValues[index] = True
        kEqualPart(arr, index+1, tempAns + str(arr[index]), tempTarget, tempSum+arr[index])

        #not take
        visitedValues[index] = False
        kEqualPart(arr, index+1, tempAns, tempTarget, tempSum)

if sum1 % k != 0:
    print("Subsets cannot be formed!")
else:
    tempTarget = sum1/k
    kEqualPart(arr, 0, '', tempTarget, 0)
    if len(ans) >= k:
        print(ans)
    else:
        print("Subsets formed but not K")
        print(ans)