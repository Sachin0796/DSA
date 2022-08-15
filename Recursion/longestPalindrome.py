tempAns=['']
def findPalindrome(s, start, end):
    if start<0 or end<0:
        return
    if start>=end:
        lengthOfPalindrome=len(s)        
        if len(tempAns[0])<lengthOfPalindrome:                             
            tempAns.pop()
            tempAns.append(s)            
            return
    if s[start]!=s[end]:
        return
    findPalindrome(s,start+1, end-1)    
s='cbbd'

for i in range(len(s)):
    for j in range(i,len(s)):                               
        findPalindrome(s[i:j],0,len(s[i:j])-1)
    
print(tempAns[0])

s= ".1"
print(s.split('.'))

print(8//10)