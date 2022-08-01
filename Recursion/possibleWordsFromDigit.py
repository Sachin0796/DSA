def possibleWords(arr, tempAns, index,a):
    if index==len(arr):        
        return tempAns
    for i in range(len(arr[index])):           
        a.append(possibleWords(arr,tempAns+arr[index][i], index+1,a))
    return a

print(possibleWords(['abc','def','ghi'],'',0,[]))