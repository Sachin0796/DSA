class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class SLinkedList:
   def __init__(self):
      self.val = None
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next

l1=SLinkedList()
l2=SLinkedList()

l1.val=ListNode(2)
e2=ListNode(4)
e3=ListNode(3)
l1.val.nextval = e2
e2.nextval = e3

l2.val=ListNode(5)
e2=ListNode(6)
e3=ListNode(4)
l2.val.nextval = e2
e2.nextval = e3

s=Solution()
print(s.addTwoNumbers(l1,l2))