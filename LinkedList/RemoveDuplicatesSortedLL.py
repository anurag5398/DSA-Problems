class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def deleteDuplicates(self, A):
        unique = set()
        prev, curr = None, A
        while curr != None:
            if curr.val not in unique:
                unique.add(curr.val)
                prev = curr
                curr = curr.next
            else:
                prev.next = curr.next
                curr = prev.next
        return A

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(3)
e = ListNode(2)
f = ListNode(6)
g = ListNode(1)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
t = Solution()
ans = t.deleteDuplicates(a)
while ans!= None:
    print(ans.val)
    ans = ans.next