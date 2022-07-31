# find all subsequences of a given string
def subSeq(s, tempAns, index):        
    if len(s)==index:
        return tempAns
    # take    
    a=subSeq(s,tempAns+s[index], index+1)        
    # not take    
    b=subSeq(s,tempAns, index+1) 
    return a+b

list1=subSeq('abc',' ',0)
print(list1)

# 2^n-1 without including empty set

# 5-31
# 4-15
# 3-7
# 2-3
# 1-1
