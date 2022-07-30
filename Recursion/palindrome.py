def palindrome(string1, start, end):
    if (start>=end):
        return 1
    if (string1[start]!=string1[end]):
        return 0
    return palindrome(string1, start+1, end-1)    

string1='abcba'
a=palindrome(string1,0,len(string1)-1)
print(a)