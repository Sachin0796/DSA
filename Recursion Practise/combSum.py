# number can be repeated in the givne combination
ans = []
def combSum(arr, index, tempAns, tempTarget, target):

    if tempTarget >= target:
        if tempTarget == target and tempAns not in ans:
            ans.append(tempAns)
        return

    if index == len(arr):
        return

    #Take
    combSum(arr, index, tempAns + str(arr[index]), tempTarget + arr[index], target)
    
    #Not take
    combSum(arr, index+1, tempAns, tempTarget, target)


arr=[4,7,8]
arr.sort()
combSum(arr,0, '', 0, 15)
print(ans)