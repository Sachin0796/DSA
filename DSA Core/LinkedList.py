# Creation of a Singly linked list
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None 


class SlinkedList:
    def __init__(self):
        headNodeAddr = None
    
sl = SlinkedList()
node1 = Node("Monday")
sl.headNodeAddr = node1 # only reference of node1 is being copied to headNodeAddr. POC is at line 22 to 33

node2 = Node("Tuesday")
node1.nextval = node2

node3 = Node("Wednesday")
node2.nextval = node3

print(node1.dataval)
print(sl.headNodeAddr.dataval)

node1.dataval = "Test"

print(node1.dataval)
print(sl.headNodeAddr.dataval)

sl.headNodeAddr.dataval = "test2"

print(node1.dataval)
print(sl.headNodeAddr.dataval)
print(type(sl.headNodeAddr))
print(type(node1.dataval))
print(type(node1.nextval))
