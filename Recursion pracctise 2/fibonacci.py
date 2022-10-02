def fibo(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    a = fibo(n-1)
    b = fibo(n-2)

    return a+b

print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(4))
print(fibo(5))
print(fibo(6))
print(fibo(7))
print(fibo(8))