from random import randint
total1=0
def function1(total,a):
    if a<=0:
        return a
    else:
        i = randint(0,6)
        total=total+1
        return function1(total,i)+function1(total,a-1-i)

function1(total1,6)
print(total1)