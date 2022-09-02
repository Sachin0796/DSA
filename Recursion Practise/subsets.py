ans = []
def subset(arr, tempAns, index):

    if index == len(arr):
        ans.append(tempAns)
        return

    # Take
    subset(arr, tempAns + arr[index], index + 1 )

    #Not take
    subset(arr, tempAns , index + 1 )

subset('abc', '', 0)
print(ans)