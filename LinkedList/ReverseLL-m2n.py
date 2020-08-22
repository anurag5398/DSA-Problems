"""
Reverse a linked list A from position B to C.
NOTE: Do it in-place and in one-pass.
"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def reversell(head, number):
    prev = None
    curr = head
    next = curr.next
    c = 0
    while curr != None and c < number:
        curr.next = prev
        prev = curr
        curr = next
        if curr:
            next = curr.next
        c+=1
    return prev, curr


def reverseBetween(A, B, C):
    if B > 1:
        temp = A
        ini = 1
        while ini < (B-1):
            temp = temp.next
            ini+=1
        start = temp
        revstart = start.next
        last, new = reversell(revstart, C-B+1)
        start.next = last
        revstart.next = new
        return A
    elif B == 1:
        revstart = A
        last, new = reversell(revstart, C-B+1)
        revstart.next = new
        return last










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

ans = reverseBetween(a, 3, 3)
while ans != None:
    print(ans.val)
    ans = ans.next