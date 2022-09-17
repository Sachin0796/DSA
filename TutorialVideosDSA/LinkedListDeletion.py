from winreg import DeleteValue


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

    def deleteValue(self, data):
        currentNode = self.headNodeAddr
        
        # empty list
        if currentNode is None:
            return

# headNode -> ("Sunday", MonAddr) ->  ("Monday", TuesAddr) - > ("Tuesday", WedAddr) - > ("Wednesday", Thursday) - > ("Thursday", None)        
# headNode ->  ("Monday", TuesAddr) - > ("Tuesday", WedAddr) - > ("Wednesday", Thursday) - > ("Thursday", None)        

        # firstNode Deletion
        if currentNode is not None:
            if currentNode.dataval == data:
                self.headNodeAddr = currentNode.nextval
                currentNode = None
                return
# headNode -> ("Sunday", MonAddr) ->  ("Monday", TuesAddr) - > ("Tuesday", WedAddr) - > ("Wednesday", Thursday) - > ("Thursday", None)   
# headNode -> ("Sunday", TuesAddr) - > ("Tuesday", WedAddr) - > ("Wednesday", Thursday) - > ("Thursday", None)   

        # deletion from the 2nd node onwards
        while currentNode is not None:
            if currentNode.dataval == data:
                break
            prev = currentNode # sun
            currentNode = currentNode.nextval # mon

        prev.nextval = currentNode.nextval
        currentNode = None

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

sl.deleteValue("Monday")
sl.deleteValue("Tuesday")
sl.deleteValue("Saturday")
sl.printList()