ans=[0]
ans[0] = 0
def maxLength(arr, tempAns, index, templength):

    if index == len(arr):
        if ans[0] < templength and templength == len(set(tempAns)):
            ans[0] = templength
        return
        
    #Take
    maxLength(arr, tempAns + arr[index], index + 1, templength + len(arr[index]))

    # not take
    maxLength(arr, tempAns , index + 1, templength)

maxLength(['cha','r','act','ers'], '', 0, 0)
print(ans[0])