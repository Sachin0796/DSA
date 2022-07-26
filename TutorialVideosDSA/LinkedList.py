class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SlinkedList:
    def __init__(self):
        self.headNodeAddr = None

    
    def printList(self):
        printNode = self.headNodeAddr
        print("Elements in the current list are:")
        while printNode is not None:
            print(printNode.dataval)
            printNode = printNode.nextval  
        
    def inBeginning(self, data):
        newNode = Node(data)        

        newNode.nextval = self.headNodeAddr
        self.headNodeAddr = newNode

    def AtEnd(self, data):
        NewNode = Node(data)

        if self.headNodeAddr is None:
            self.headNodeAddr = NewNode
            return

        currentNode = self.headNodeAddr
        while currentNode.nextval is  not None:
            currentNode = currentNode.nextval
        currentNode.nextval = NewNode        

    def InBetween(self, RefNode, data):
        Newnode = Node(data)

        if RefNode is None:
            print("RefNode is not in the list")
            return
        Newnode.nextval = RefNode.nextval
        RefNode.nextval = Newnode                        


sl = SlinkedList()

node1 = Node("Monday")

sl.headNodeAddr = node1 # reference copy

node2 = Node("Tuesday")
node3 = Node("Wednesday")

node1.nextval = node2
node2.nextval = node3

# sl.printList()
sl.inBeginning("Sunday")
# sl.printList()

sl.AtEnd("Friday")
# sl.printList()

sl.InBetween(node3 , "Thursday")
# sl.printList()

sl.AtEnd("Saturday")
# sl.printList()
