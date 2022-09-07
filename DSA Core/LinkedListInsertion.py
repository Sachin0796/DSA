# Traversing through a Singly linked list
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None 

class SlinkedList:
    def __init__(self):
        headNodeAddr = None

    # traversing function
    def printList(self):
        printNode = self.headNodeAddr
        print("\nElements in the current list are:")
        while printNode is not None:
            print(printNode.dataval)
            printNode = printNode.nextval

    def AtBeginning(self, data):
        NewNode = Node(data)

        NewNode.nextval = sl.headNodeAddr
        sl.headNodeAddr = NewNode
    
    def AtEnd(self, data):
        NewNode = Node(data)
        
        if self.headNodeAddr is None:
            self.headNodeAddr = NewNode

        printNode = self.headNodeAddr
        while printNode.nextval is not None:
            printNode = printNode.nextval 
        printNode.nextval = NewNode


# headNode("Node1Addr") - > ("Sunday", MonAddr) - > ("Monday", TuesAddr) - > ("Tuesday", WedAddr) - > ("Wednesday", None)

# NEW_NODE - ("Friday", None)

# NEWLIST
# headNode("Node1Addr") - > ("Sunday", MonAddr) - > ("Monday", TuesAddr) - > ("Tuesday", WedAddr) - > ("Wednesday", FriAddr) - > ("Friday", None)        

    def inBetween(self, RefNode, data):
        if RefNode is None:
            print("RefNode is not in the list")

        NewNode = Node(data)
        NewNode.nextval = RefNode.nextval
        RefNode.nextval = NewNode


sl= SlinkedList()
node1 = Node("Monday")
sl.headNodeAddr = node1 # only reference of node1 is being copied to headNodeAddr

node2 = Node("Tuesday")
node3 = Node("Wednesday")

node1.nextval = node2
node2.nextval = node3

# print(node1.dataval)
# print(sl.headNodeAddr.dataval)

# node1.dataval = "Test"

# print(node1.dataval)
# print(sl.headNodeAddr.dataval)

# sl.headNodeAddr.dataval = "test2"

# print(node1.dataval)
# print(sl.headNodeAddr.dataval)
# print(type(sl.headNodeAddr))
# print(type(node1.dataval))
# print(type(node1.nextval))

# sl.printList()



# OLDLIST
# headNode("Node1Addr") - > ("Monday", TuesAddr) - > ("Tuesday", WedAddr) - > ("Wednesday", None)

# NEW_NODE - ("Sunday", None) # to add in beginning

# NEWLIST
# headNode("Node1Addr") - > ("Sunday", MonAddr) - > ("Monday", TuesAddr) - > ("Tuesday", WedAddr) - > ("Wednesday", None)

sl.AtBeginning("Sunday")
sl.printList()

# NEW_NODE - ("Friday", None)

# NEWLIST
# headNode("Node1Addr") - > ("Sunday", MonAddr) - > ("Monday", TuesAddr) - > ("Tuesday", WedAddr) - > ("Wednesday", FriAddr) - > ("Friday", None)

sl.AtEnd("Friday")
sl.printList()

# NEW_NODE - ("Thursday", None)

# NEWLIST
# headNode("Node1Addr") - > ("Sunday", MonAddr) - > ("Monday", TuesAddr) - > ("Tuesday", WedAddr) - > ("Wednesday", Thursday) - > ("Thursday", FriAddr) - > ("Friday", None)

sl.inBetween(node3,"Thursday")
sl.printList()

sl.AtEnd("Saturday")
sl.printList()