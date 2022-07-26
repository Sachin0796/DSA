"""
In a simple queue, insertion takes place at the rear and removal occurs at the front. It strictly follows the FIFO (First in First out) rule.
"""

class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        if(len(self.queue)==0):
            print("Queue is empty")
            return None
        return self.queue.pop(0)
    def display_queue(self):
        print(self.queue)
    def queue_size(self):
        print("Length of the queue is :",len(self.queue))

q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.display_queue()
q.queue_size()
q.dequeue()
q.dequeue()
q.dequeue()
q.display_queue()
q.queue_size()
q.dequeue()
q.dequeue()
q.dequeue()
q.display_queue()
q.queue_size()