"""
Given a singly linked list A, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.
"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class Solution:
    def findmid(self, head):
        s, f = head, head
        while f.next != None:
            s = s.next
            f = f.next
            if f.next != None:
                f = f.next
        return s

    def reversell(self, head):
        prev = None
        curr = head
        next = curr.next
        while curr:
            curr.next = prev
            prev = curr
            curr = next
            if curr:
                next = curr.next
        return prev

    def lPalin(self, A):
        if A.next is None:
            return 0

        #check mid
        s = self.findmid(A)

        temp = A
        while temp.next != s:
            temp = temp.next
        temp.next = None

        two = self.reversell(s)
        one = A

        while one:
            if one.val != two.val:
                return 0
            one = one.next
            two = two.next
        return 1


a = ListNode(1)
b = ListNode(1)
c = ListNode(2)
d = ListNode(1)
e = ListNode(3)
f = ListNode(2)
g = ListNode(1)
#a.next = b
#b.next = c
c.next = d
#d.next = e
e.next = f
f.next = g

t = Solution()
print(t.lPalin(a))