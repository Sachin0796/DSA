ansList=[]
def findNumberSequence(direction):
    ans=[0]*2
    ans[0] = 0
    ans[1] = 2**len(direction)
    mydict=dict()     
    index=0   
    print(len(direction))
    while index < len(direction):                          
        tempAns=(ans[0] + ans[1])//2
        
        mydict[index] = tempAns
        
        if direction[index] == 'L':
            ans[1] = tempAns
        elif direction[index] == 'R':
            ans[0] = tempAns        
        index+=1                                
    for i in sorted(mydict.values()):
        ansList.append(list(mydict.values()).index(i)+1)
    return ansList

findNumberSequence('LLLL')

print(ansList)