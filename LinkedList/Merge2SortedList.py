"""
Merge two sorted linked lists A and B and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.
"""
class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class ll:
    def __init__(self):
        self.head = None
        self.last = None
    def addnode(self, node):
        if self.head:
            self.last.next = node
            self.last = node
        else:
            self.head = node
            self.last = node
    def wrapup(self):
        self.last.next = None

class Solution:
    def mergeTwoLists(self, A, B):
        newll = ll()
        a, b = A, B
        while a and b:
            if a.val <= b.val:
                newll.addnode(a)
                a = a.next
            else:
                newll.addnode(b)
                b = b.next
        while a:
            newll.addnode(a)
            a = a.next
        while b:
            newll.addnode(b)
            b = b.next
        newll.wrapup()
        return newll.head    
