# Combinations of k numbers out of the range 1 to N

# K = 3 = 1,2,3
# N = 2

# output = 1,2 and 2,3 and 1,3

ans = []
def nRangeCombination(k, n, tempAns, index):    
    if len(tempAns) == n:
        ans.append(tempAns)        
        return    
    if index == len(k):        
        return
    if len(tempAns) == 0 and len(k) - index < n:        
        return     
    nRangeCombination(k, n, tempAns+k[index], index+1)    
    nRangeCombination(k, n, tempAns, index+1)
    
nRangeCombination(['1','2','3','4'], 3, '', 0)
print(ans)