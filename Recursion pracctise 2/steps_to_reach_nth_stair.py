def stepsToReach(stepNumber):
    
    if stepNumber == 1 or stepNumber == 2:
        return stepNumber
    
    a = stepsToReach(stepNumber-1)
    b = stepsToReach(stepNumber-2)

    return a + b

print(stepsToReach(10)) 