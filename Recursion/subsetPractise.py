ans=[]
def subsetPractise(arr, tempAns, index):
    if len(arr) == index:
        ans.append(tempAns)
        return
    # take
    subsetPractise(arr, tempAns+arr[index], index+1)
    # not take
    subsetPractise(arr, tempAns, index+1)
    
subsetPractise(['1','2','3'], '', 0)
print(ans)