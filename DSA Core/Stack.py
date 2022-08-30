"""
A stack is a linear data structure that follows the principle of Last In First Out (LIFO). This means the last element inserted inside the stack is removed first.
"""

def create_stack():
    stack=[]
    return stack

def empty_stack(stack):
    return len(stack)==0

def push(stack, item):
    stack.append(item)
    print(f"Pushed item: {item}")

def pop(stack):
    if (empty_stack(stack)==True):
        print("Stack is empty")
        return
    return stack.pop()
def peek(stack):
    return stack[len(stack)-1]

stack=create_stack()
push(stack,1)
push(stack,2)
push(stack,3)
print("**********************************")
print("Peeked Item:",peek(stack))
print("Popped Item:",pop(stack))
print("Peeked Item:",peek(stack))
print("Popped Item:",pop(stack))
print("Peeked Item:",peek(stack))
print("Popped Item:",pop(stack))
print("Popped Item:",pop(stack))
print("Popped Item:",pop(stack))

# For the array-based implementation of a stack, the push and pop operations take constant time, i.e. O(1).
