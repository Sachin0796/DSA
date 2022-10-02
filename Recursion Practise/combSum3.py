#for given range of numbers, find the n numbers that has sum equal to given target
ans = []
def combSum3(arr, target, tempAns, index, tempTarget, n):

    if index == len(arr):
        return
    
    if tempTarget == target and len(tempAns) == n:
        ans.append(tempAns)
        return

    if tempTarget > target:
        return

    combSum3(arr, target, tempAns + str(arr[index]), index + 1, tempTarget + arr[index], n)
    combSum3(arr, target, tempAns, index + 1, tempTarget, n)
lst = range(1, 50)
n = 3

combSum3(lst, 24, '', 0, 0, n)
print(ans)