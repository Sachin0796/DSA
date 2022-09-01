def fibonacci(n):

    if n < 0:
        return False
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    #n - 1
    a = fibonacci(n-1)
    #n - 2
    b = fibonacci(n-2)

    return a + b

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))
print(fibonacci(9))
print(fibonacci(10))
print(fibonacci(11))
