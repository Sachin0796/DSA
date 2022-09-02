ans = []
def uniqSubset(arr, index, tempAns):

    if index ==  len(arr):
        if tempAns not in ans:
            ans.append(tempAns)
        return

    # take
    uniqSubset(arr, index + 1, tempAns + arr[index])

    #not take
    uniqSubset(arr, index + 1, tempAns)

uniqSubset('aac', 0, '')
print(ans)