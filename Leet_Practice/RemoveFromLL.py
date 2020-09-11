"""
Remove all elements from a linked list of integers that have value val.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev, curr = None, head
        print("prev and curr set")
        while curr and curr.val == val:
            curr = curr.next
        new_head = curr
        prev, curr = new_head, new_head.next
        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = prev.next
            else:
                prev, curr = curr, curr.next
        return new_head

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(2)

a.next = b
b.next = c
c.next = d
t = Solution()
new = t.removeElements(a, 2)
while new:
    print(new.val)
    new = new.next