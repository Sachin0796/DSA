ans = ['']
def longestPalindrome(str, start, end):            
    if start < 0 or end < 0:
        return

    if start >= end:
        if len(str) > len(ans[0]):                   
            ans.pop()
            ans.append(str)
        return
    
    if str[start] != str[end]:
        return

    longestPalindrome(str, start + 1, end - 1)

str = 'aab'
for i in range(len(str)):
    for j in range(i, len(str)):
        # print(str[i:j], 0, len(str[i:j])-1)
        longestPalindrome(str[i:j+1], 0, len(str[i:j+1])-1)        

print(ans[0])