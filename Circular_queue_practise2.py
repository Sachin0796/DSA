"""
A circular queue is the extended version of a regular queue where the last element is connected to the first element. Thus forming a circle-like structure.
The circular queue solves the major limitation of the normal queue. In a normal queue, after a bit of insertion and deletion, there will be non-usable empty space.
"""
class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.head=-1
        self.tail=-1
        self.cQueue=[None]*size
    def enQueue(self,item):
        # cQueue Overflow
        if(self.tail==(self.head+1)%self.size):
            print("Queue is full !")
            return
        if self.head==-1:
            self.head=self.tail=0
            self.cQueue[self.head]=item
            print("Inserted Element:", item)
        else:
            self.head=(self.head+1)%self.size
            self.cQueue[self.head]=item
            print("Inserted Element:", item)
    def deQueue(self):
        # cQueue Underflow
        if (self.head==-1):
            print("Circular Queue is empty")
        if self.head==self.tail:
            item=self.cQueue[self.head]
            self.cQueue[self.head]='NULL'
            self.head=self.tail=-1
            print("Removed Element:", item)
            return item
        else:
            item=self.cQueue[self.tail]
            self.cQueue[self.tail]='NULL'
            self.tail=(self.tail+1)%self.size
            print("Removed Element:", item)
            return item
    def printCQueue(self):
        print("Current item in the queue are:", self.cQueue)

q=CircularQueue(5)
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
q.printCQueue()
q.enQueue(4)
q.enQueue(5)
q.enQueue(6)
q.printCQueue()
q.deQueue()
q.deQueue()
q.deQueue()
q.printCQueue()
q.enQueue(7)
q.enQueue(8)
q.enQueue(9)
q.printCQueue()
q.deQueue()
q.deQueue()
q.printCQueue()