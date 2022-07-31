# finding all subset
# Not working
# def subset(arr, tempAns, index):
#     if index==len(tempAns):
#         return tempAns
#     a=tempAns.append(arr[index])
#     subset(arr,tempAns,index+1)
#     b=tempAns.pop()
#     subset(arr, tempAns, index+1)
#     return a, b

# print(subset('123',[],0))

def subset1(arr, tempAns, index):
    if index==len(arr):
        return tempAns
    #take
    a=subset1(arr, tempAns+arr[index],index+1)
    #not take
    b=subset1(arr, tempAns,index+1)
    return a+' '+b

print(subset1('123','',0))