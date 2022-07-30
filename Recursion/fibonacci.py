def fibonacci(number):            
    if number==0:
        return 0
    elif number==1:
        return 1
    else:                   
        fn_1=fibonacci(number-1)
        fn_2=fibonacci(number-2)
        return fn_1+fn_2
    
print(fibonacci(8))
# 0 1 2 3 4 5 6 
# 0 1 1 2 3 5 8
                       