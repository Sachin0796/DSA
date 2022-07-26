"""
In a simple queue, insertion takes place at the rear and removal occurs at the front. It strictly follows the FIFO (First in First out) rule.

Below queue is configured in such a way that:
1. U can insert upmost 5 elements
2. Display will only show the elements which are not popped yet.
"""
class Queue:
    def __init__(self,k):
        self.k=k
        self.queue=[None]*k
        self.head=self.tail=-1
        self.popped_list=[]
    def push(self,item):
        if (self.tail==self.k-1):
            print("Queue is full")
        else:
            if(self.head==-1):
                self.head = self.head + 1
            self.tail = self.tail + 1
            self.queue[self.tail] = item
            print("Pushed Item:", item)
    def pop(self):
        if(self.head==-1):
            print("Queue is empty")
        else:
            temp=self.queue[self.head]
            if(self.head==self.tail):
                self.head=self.tail=-1
            else:
                self.head = self.head + 1
            self.popped_list.append(temp)
            print(f"Popped Item: {temp}")
            # print(self.head,self.tail)
            return temp
    def print_queue(self):
        if (self.head == -1):
            print("Circular queue is empty")
        else:
            print("Items in the Circular queue are:")
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
        print("")
    def size_queue(self):
        return len(self.queue)

q=Queue(4)
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)
q.print_queue()
q.pop()
q.pop()
q.pop()
q.pop()
q.pop()
q.print_queue()
q.push(6)
q.push(7)
q.push(8)
q.print_queue()
# q.pop()
q.pop()
q.push(9)
q.print_queue()
q.pop()
q.push(10)
q.print_queue()
# q=Queue(int(input("Enter the maximum elements you want to push in the list:")))
# while(True):
#     a=int(input("Please select the action you want to perform:\n1. Insert in the queue.\n"
#           "2. Remove from the queue\n"
#           "3. Display the current items in the queue\n"
#            "4. Quit\n"))
#     if(a==1):
#         item=int(input("Enter the element you want to add in the queue:"))
#         q.push(item)
#     elif(a==2):
#         q.pop()
#     elif(a==3):
#         q.print_queue()
#     elif(a==4):
#         exit(0)
#     else:
#         print("Please provide the correct input")

