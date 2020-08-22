"""
Given a singly linked list A
 A: A0 → A1 → … → An-1 → An 
reorder it to:
 A0 → An → A1 → An-1 → A2 → An-2 → … 
You must do this in-place without altering the nodes' values.
"""
#the last element was going into loop. So after number of nodes calculation. Found the last to occur node, and at last moved its next to None.

import math
import time
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversell(self, head):
        if head:
            prev, curr = None, head
            next = curr.next
            while curr != None:
                curr.next = prev
                prev = curr
                curr = next
                if curr:
                    next = curr.next
            return prev
        else:
            return None

    def solve(self, A):
        head = A
        temp, count = head, 0
        while temp != None:
            temp = temp.next
            count+=1
        if count == 1:
            return head

        #print("count ",count)
        mid = math.ceil(count/2)
        secondhead = head
        while mid > 0:
            secondhead = secondhead.next
            mid-=1
        if count %2 == 0:
            lastnode = secondhead
        else:
            lastnode = head
            while lastnode.next != secondhead:
                lastnode = lastnode.next


        secondhead = self.reversell(secondhead)
        #print(head.val, secondhead.val)


        curr1, next1 = head, head.next
        curr2, next2 = secondhead, secondhead.next
        while curr1 != None and curr2 != None:
            curr1.next = curr2
            curr2.next = next1
            curr1 = next1
            curr2 = next2
            if curr1:
                next1 = curr1.next
            if curr2:
                next2 = curr2.next
        lastnode.next = None
        return head

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
f.next = g

t = Solution()
ans = t.solve(a)
while ans != None:
    print(ans.val)
    ans = ans.next
