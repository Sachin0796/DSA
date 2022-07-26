"""
A stack is a linear data structure that follows the principle of Last In First Out (LIFO). This means the last element inserted inside the stack is removed first.
"""


def createStack():
    stack=[]
    return stack

def push(stack,item):
    stack.append(item)
    print("Pushed Item: ",item)

def pop(stack):
    if (len(stack)==0):        
            print ("Stack is empty")
            return
    item=stack.pop()
    print("Popped Item: ",item)

def showStack(stack):
    if (len(stack)==0):        
        print ("Nothing to show")
        return
    print("My Stack is: ",stack)

myStack=createStack()
push(myStack,1)
push(myStack,2)
push(myStack,3)
push(myStack,4)
push(myStack,5)
showStack(myStack)
pop(myStack)
pop(myStack)
pop(myStack)
showStack(myStack)
push(myStack,6)
push(myStack,7)
push(myStack,8)
showStack(myStack)
pop(myStack)
pop(myStack)
pop(myStack)
showStack(myStack)
pop(myStack)
pop(myStack)
pop(myStack)
showStack(myStack)