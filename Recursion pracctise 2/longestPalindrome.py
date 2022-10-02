ans = ['']
def longestPalindrome(string, start, end):
    
    if start>=end:
        if len(string) > len(ans[0]):
            ans[0] = string
        return
    
    if string[start] ==string[end]:
        longestPalindrome(string, start+1, end-1)

str = 'aaaccccbbbbb'
for i in range(len(str)):
    for j in range(i, len(str)+1):
        longestPalindrome(str[i:j], 0, len(str[i:j])-1)


print(ans[0])