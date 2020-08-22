"""
Given a doubly linked list of integers with one pointer of each node pointing to the next node (just like in a single link list) while the second pointer, however, can point to any node in the list and not just the previous node.
You have to create a copy of this list and return the head pointer of the duplicated list.
"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None

def printll(head):
    temp = head
    while temp != None:
        if temp.random:
            ran = temp.random.val
        else:
            ran = None
        print("node {} random {}".format(temp.val, ran))
        temp = temp.next

def clonelist(A):
    #printll(A)

    #print("add extra nodes")
    temp = A
    while temp != None:
        a = ListNode(temp.val)
        a.next = temp.next
        temp.next = a
        temp = a.next
    #printll(A)

    #print("copy random links")
    ot, nt = A, A.next
    while ot != None:
        nt.random = ot.random.next
        ot = ot.next.next
        nt = nt.next
        if nt:
            nt = nt.next
    #printll(A)

    #print("remove old")
    nh = A.next
    temp = nh
    while temp.next != None:
        temp.next = temp.next.next
        temp = temp.next

    #printll(nh)
    return nh
    




a = ListNode(1)
b = ListNode(2)
c = ListNode(3)

a.next = b
a.random = c
b.next = c
b.random = a
c.random = c

temp = a
while temp:
    print(temp)
    temp = temp.next
ans = clonelist(a)
while ans:
    print(ans)
    ans = ans.next
