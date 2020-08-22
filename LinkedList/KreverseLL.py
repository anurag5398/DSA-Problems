"""
Given a singly linked list A and an integer B, reverse the nodes of the list B at a time and return modified linked list.
"""
class listNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def reversell(head, k):
    if head:
        if head.next is None:
            return head, None
        
        prev, curr, next = None, head, head.next
        while k > 0 and curr != None:
            curr.next = prev
            prev = curr
            curr = next
            if next != None:
                next = curr.next
            k-=1
        return prev, curr
    #temp = prev
    #print(" next ",curr, prev.val)
    #while prev != None:
    #    print(prev.val)
    #    prev = prev.next

def solve(A, B):
    start = A
    ns = start
    last, new = reversell(ns, B)
    ns = new
    newhead = last
    while ns != None:
        #print(ns.val)
        last, new = reversell(ns, B)
        start.next = last
        start = ns
        ns = new
    return newhead




    

a = listNode(1)
b = listNode(2)
c = listNode(3)
d = listNode(4)
e = listNode(5)
f = listNode(6)
g = listNode(7)
h = listNode(8)
i = listNode(9)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
#f.next = g
#g.next = h
#h.next = i

#prev, curr =reversell(a, 3)

new = solve(a, 4)
#while new != None:
#    print(new.val)

