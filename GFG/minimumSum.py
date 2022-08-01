def minSum(a, b, tempSum, index, takeMin):
    a.sort()
    b.sort()
    result=0
    for i in range(len(a)):
        result += a[i]*b[len(b)-1-i]
    return result


print(minSum([3, 1, 1], [6, 5, 4], 0, 0, 50000))