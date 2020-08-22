"""
Given a linked list A and a value B, partition it such that all nodes less than B come before nodes greater than or equal to B.
You should preserve the original relative order of the nodes in each of the two partitions.
"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class ll:
    def __init__(self):
        self.head = None
        self.last = None
    def addnode(self, node):
        if self.head is None:
            self.head = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
    def complete(self):
        self.last.next = None

class Solution:
    def partition(self, A, B):
        if A.next is None:
            return A
        l2 = ll()
        temp = A
        while temp and temp.val >= B:
            l2.addnode(temp)
            temp = temp.next
        nh = temp
        
        while temp and temp.next:
            if temp.next.val >= B:
                l2.addnode(temp.next)
                temp.next = temp.next.next
            else:
                temp = temp.next
        if temp:
            temp.next = l2.head
        else:
            nh = l2.head
        l2.complete()
        return nh


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(2)
g = ListNode(1)
a.next = b
b.next = c
c.next = d
d.next = e
#e.next = f
f.next = g

t = Solution()
a = t.partition(a, 1)
while a:
    print(a.val)
    a = a.next