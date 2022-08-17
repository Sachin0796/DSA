a=[]
def possibleWords(arr, tempAns, index, a):
    if index==len(arr):        
        a.append(tempAns)
        return
    for i in range(len(arr[index])):           
        possibleWords(arr, tempAns+arr[index][i], index+1, a)

possibleWords(['abc','def'],'',0, a)
print(a)