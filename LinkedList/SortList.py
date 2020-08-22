"""
Sort a linked list, A in O(n log n) time using constant space complexity.
"""
#QS
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def qs(start, last):
    if start == last:
        return start

    i = ListNode(0)
    i.next = start
    pivot = last
    j = start

    while j != pivot:
        if j.val <= pivot.val:
            i = i.next
            i.val, j.val = j.val, i.val
        j = j.next
    i = i.next
    i.val, pivot.val = pivot.val, i.val
    return i

def solve(l, r):
    pos = qs(l, r)
    if l != pos:
        s = l
        e = s
        while e.next != pos:
            e = e.next
        solve(s, e)
    if pos.next and pos != r:
        s = pos.next
        e = s
        while e.next and e != r:
            e = e.next
        solve(s, e)




a = ListNode(3)
b = ListNode(4)
c = ListNode(2)
d = ListNode(8)
e = ListNode(5)
f = ListNode(3)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

solve(a,f)
temp = a
while temp != None:
    print(temp.val)
    temp = temp.next