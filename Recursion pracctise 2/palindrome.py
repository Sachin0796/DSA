def palin(string, start, end):
    if start >= end:
        return True
    
    if string[start] == string[end]:
        return palin(string, start+1, end-1)
    else:
        return False

s='abb'
a = palin(s, 0, len(s)-1)
print(a)