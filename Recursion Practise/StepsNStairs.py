def countSteps(n):

    if n == 1 or n == 2:
        return n

    # from n-1 step
    a = countSteps(n-1)

    # from n-2 step
    b = countSteps(n-2)
    
    return a + b

print(countSteps(10))