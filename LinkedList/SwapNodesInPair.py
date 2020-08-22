"""
Given a linked list A, swap every two adjacent nodes and return its head.
NOTE: Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
"""
import time
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def swap(self, ns):
        curr = ns.next
        if curr is None:
            return ns, None
        next = curr.next
        curr.next = ns
        ns.next = None
        return curr, next

    def swapPairs(self, A):
        start, ns = A, A
        newhead, new = self.swap(ns)
        ns = new

        while ns != None:
            last, new = self.swap(ns)
            start.next = last
            start = ns
            ns = new
        return newhead

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
g = ListNode(7)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
#f.next = g
t = Solution()
ans = t.swapPairs(a)
while ans:
    print(ans.val)
    ans = ans.next
    