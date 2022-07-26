"""
In a simple queue, insertion takes place at the rear and removal occurs at the front. It strictly follows the FIFO (First in First out) rule.
"""

"""
Queue with limited elements.
Why is this not the circular queue?
"""

class Queue:
    def __init__(self,size):
        self.size=size
        self.queue=[]
    def enQueue(self,item):
        if len(self.queue)==self.size:
            print("Queue is full !")
            return
        self.queue.append(item)
        print("Added element:", item)
    def deQueue(self):
        if len(self.queue)==0:
            print("Queue is empty !")
            return
        item=self.queue.pop(0)
        print("Removed element:", item)
    
    def showQueue(self):
        if len(self.queue)==0:
            print("Nothing to show !")
            return
        print("My queue is:", self.queue)

q=Queue(5)
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
q.enQueue(4)
q.enQueue(5)
q.enQueue(6) # Queue is full !
q.showQueue() # My queue is: [1, 2, 3, 4, 5]
q.deQueue()
q.deQueue()
q.deQueue()
q.showQueue() # My queue is: [4, 5]
q.enQueue(6)
q.enQueue(7)
q.enQueue(8)
q.showQueue() # My queue is: [4, 5, 6, 7, 8]
q.deQueue()
q.deQueue()
q.deQueue()
q.enQueue(9)
q.enQueue(10)
q.enQueue(11)
q.showQueue() # My queue is: [7, 8, 9, 10, 11]
q.deQueue()
q.deQueue()
q.deQueue()
q.enQueue(12)
q.enQueue(13)
q.enQueue(14)
q.enQueue(15) # Queue is full !
q.enQueue(16) # Queue is full !
q.enQueue(17) # Queue is full !
q.showQueue() # My queue is: [10, 11, 12, 13, 14]     
q.deQueue()
q.deQueue()
q.deQueue()
q.deQueue()
q.deQueue()
q.deQueue() # Queue is empty !
q.showQueue() # Nothing to show !