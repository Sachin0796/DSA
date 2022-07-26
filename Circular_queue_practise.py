"""
A circular queue is the extended version of a regular queue where the last element is connected to the first element. Thus forming a circle-like structure.
The circular queue solves the major limitation of the normal queue. In a normal queue, after a bit of insertion and deletion, there will be non-usable empty space.
"""
class Circular_queue:
    def __init__(self,k):
        self.k=k
        self.Circular_queue=[None]*self.k
        self.head=self.tail=-1
    def enqueue(self,item):
        if((self.tail+1)%self.k==self.head):
            print("Queue is full\n")
        elif(self.head==-1):
            self.head+=1
            self.tail+=1
            self.Circular_queue[self.head]=item
            print(f"Inserted Element: {item}")
        else:
            self.tail=(self.tail+1)%self.k
            self.Circular_queue[self.tail]=item
            print(f"Inserted Element: {item}")
    # if((self.head==0 and self.tail==self.k-1) or (self.head==self.tail+1)):
    def dequeue(self):
        if(self.head==-1):
            print("Queue is empty\n")
        elif(self.head==self.tail):
            temp=self.Circular_queue[self.head]
            self.head = -1
            self.tail = -1
            print(f"Removed Element: {temp}")
            return temp
        else:
            temp=self.Circular_queue[self.head]
            self.head=(self.head+1)%self.k
            print(f"Removed Element: {temp}")
            return temp
    def print_Circular_queue(self):
        if(self.head==-1):
            print("Circular queue is empty")
        elif(self.head<=self.tail):
            print("Items in the Circular queue are:")
            for i in range(self.head,self.tail+1):
                print(self.Circular_queue[i],end=" ")
                # print(self.head,self.tail)
        else:
            print("Items in the Circular queue are:")
            for i in range(self.head,self.k):
                print(self.Circular_queue[i], end=" ")
                # print(self.head, self.tail)
            for i in range(0,self.tail+1):
                print(self.Circular_queue[i], end=" ")
                # print(self.head, self.tail)
        print("")

q=Circular_queue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.print_Circular_queue()
q.dequeue()
q.dequeue()
q.dequeue()
q.print_Circular_queue()
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.print_Circular_queue()
q.dequeue()
q.dequeue()
q.print_Circular_queue()
q.enqueue(9)
q.enqueue(10)
q.print_Circular_queue()
# q.enqueue(11)
# q.print_Circular_queue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.print_Circular_queue()
