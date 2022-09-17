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

    def inBetween(self, RefNode, data):
        if RefNode is None:
            print("RefNode is not in the list")

        NewNode = Node(data)
        NewNode.nextval = RefNode.nextval
        RefNode.nextval = NewNode

# headnode -> ("Sunday", MonAddr) - > ("Monday", TuesAddr) - > ("Tuesday", WedAddr) - > ("Wednesday", Thursday) - > ("Thursday", None) 
    def deleteValue(self, data):
        currentNode = self.headNodeAddr

        # empty list
        if currentNode is None:
            return
# headnode ->  ("Monday", TuesAddr) - > ("Tuesday", WedAddr) - > ("Wednesday", Thursday) - > ("Thursday", None)        
        #firstNode deletion
        if currentNode is not None:
            if currentNode.dataval == data:
                self.headNodeAddr = currentNode.nextval
                currentNode = None
                return


# headnode -> ("Sunday", MonAddr) ->  ("Monday", TuesAddr) - > ("Tuesday", WedAddr) - > ("Wednesday", Thursday) - > ("Thursday", None)
        #rest of the cases
        while currentNode:
            if currentNode.dataval == data:
                break
            prev = currentNode
            currentNode = currentNode.nextval

        prev.nextval = currentNode.nextval
        currentNode = None
        return


sl= SlinkedList()
node1 = Node("Monday")
sl.headNodeAddr = node1 # only reference of node1 is being copied to headNodeAddr

node2 = Node("Tuesday")
node3 = Node("Wednesday")

node1.nextval = node2
node2.nextval = node3

sl.AtBeginning("Sunday")
# sl.printList()

sl.AtEnd("Friday")
# sl.printList()

sl.inBetween(node3,"Thursday")
# sl.printList()

sl.AtEnd("Saturday")
# sl.printList()

sl.deleteValue("Sunday")
# headnode -> ("Sunday", MonAddr) - > ("Monday", TuesAddr) - > ("Tuesday", WedAddr) - > ("Wednesday", Thursday) - > ("Thursday", None) 
sl.printList()