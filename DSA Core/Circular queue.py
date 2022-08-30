"""
A circular queue is the extended version of a regular queue where the last element is connected to the first element. Thus forming a circle-like structure.
The circular queue solves the major limitation of the normal queue. In a normal queue, after a bit of insertion and deletion, there will be non-usable empty space.
"""
class MyCircularQueue():
    def __init__(self,k):
        self.k=k
        self.queue=[None]*k
        self.head=self.tail=-1
    def enqueue(self,data):
        if((self.tail+1)%self.k==self.head):
            print("The circular queue is full")
        elif(self.head==-1):
            self.head=0
            self.tail=0
            self.queue[self.head]=data
            print("Element Inserted")
        else:
            self.tail=(self.tail+1)%self.k
            self.queue[self.tail]=data
            print("Element Inserted")
    def dequeue(self):
        if(self.head==-1):
            print("The circular queue is empty")
        elif(self.head==self.tail):
            temp=self.queue[self.head]
            self.head=-1
            self.tail=-1
            print("Element Removed")
            return temp
        else:
            temp = self.queue[self.head]
            self.head=(self.head+1)%self.k
            print("Element Removed")
            return temp
    def print_circular_queue(self):
        if (self.head==-1):
            print("Circular queue is empty..!!")
        elif(self.head<=self.tail):
            print("Elements in the queue are:")
            for i in range(self.head,self.tail+1):
                print(self.queue[i],end=" ")
        else:
            print("Elements in the queue are:")
            for i in range(self.head,self.k):
                print(self.queue[i], end=" ")
            for i in range(0,self.tail+1):
                print(self.queue[i], end=" ")
        print("")
q=MyCircularQueue(5)
# q.dequeue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.print_circular_queue()
q.dequeue()
q.dequeue()
q.dequeue()
q.print_circular_queue()
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
q.print_circular_queue()
q.dequeue()
q.dequeue()
q.print_circular_queue()