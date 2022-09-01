def steps(stair):
    if stair==1:
        return 1
    elif stair==2:
        return 2
    else:
        s1=steps(stair-1)
        s2=steps(stair-2)
        return s1+s2

print(steps(10))
