"""
In a simple queue, insertion takes place at the rear and removal occurs at the front. It strictly follows the FIFO (First in First out) rule.
"""
#Using function
def createQueue():
    queue=[]
    return queue

def enqueue(queue,item):
    queue.append(item)
    print("Item added in the queue:", item)

def dequeue(queue):
    if (len(queue)==0):
        print("Queue is empty")
        return
    item=queue.pop(0)
    print("Removed element, ",item)

def showQueue(queue):
    if (len(queue)==0):
        print("Nothing to show")  
        return
    print("My queue is: ",queue)

myQueue=createQueue()
enqueue(myQueue,1)
enqueue(myQueue,2)
enqueue(myQueue,3)
enqueue(myQueue,4)
enqueue(myQueue,5)
showQueue(myQueue)
dequeue(myQueue)
dequeue(myQueue)
dequeue(myQueue)
showQueue(myQueue)
enqueue(myQueue,6)
enqueue(myQueue,7)
enqueue(myQueue,8)
showQueue(myQueue)
dequeue(myQueue)
dequeue(myQueue)
dequeue(myQueue)
dequeue(myQueue)
dequeue(myQueue)
dequeue(myQueue)
showQueue(myQueue)

# using class

class Queue:
    def __init__(self):
        self.queue=[]
    def enQueue(self,item):
        self.queue.append(item)
        print("Added element:",item)
    def deQueue(self):
        if (len(self.queue)==0):
            print("Queue is empty")
            return 
        item=self.queue.pop(0)
        print("Removed Element:",item)
    def showQueue(self):
        if (len(self.queue)==0):
            print("Nothng to show")
            return
        print("My queue is:",self.queue)
    
q=Queue()
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
q.enQueue(4)
q.enQueue(5)
q.showQueue()
q.deQueue()
q.deQueue()
q.deQueue()
q.showQueue()
q.enQueue(6)
q.enQueue(7)
q.enQueue(8)
q.showQueue()
q.deQueue()
q.deQueue()
q.deQueue()
q.deQueue()
q.deQueue()
q.deQueue()
q.showQueue()