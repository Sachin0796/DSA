def checkPalin(str, l, r):
    
    if l >= r:        
        return True
    
    if str[l] != str[r]:
        return False
    
    return checkPalin(str, l + 1, r - 1)

s = 'malayalam'
print(checkPalin(s, 0, len(s)-1))

