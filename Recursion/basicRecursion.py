def sum(n):
    if n<0:
        print("Sum not found !")
        return 
    elif n==0: # base condition
        return 0
    return n + sum(n-1) # small calculation and recursive call

print("Sum:",sum(5))

def fact(n):
    if n<0:
        print("Factorial not found !")
        return 
    elif n==1 or n==0: # base condition
        return 1
    return n * fact(n-1) # small calculation and recursive call

print("Fact:",fact(5))

def powerNof2(n):
    if n<0:
        print("Negative power not handled !")
        return 
    elif n==0: # base condition
        return 1
    return 2*powerNof2(n-1)

print("Power of n:",powerNof2(1))