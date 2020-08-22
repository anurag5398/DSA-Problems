"""
Given a linked list of integers. Find and return the length of the longest palindrome list that exists in that linked list.
A palindrome list is a list that reads the same backward and forward.
Expected memory complexity : O(1)
"""
#expected sc - 1, used - n

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class DoubleNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class Solution:
    def convertDouble(self, head):
        curr = head
        s = DoubleNode(curr.val)
        nh = s
        while curr.next != None:
            curr = curr.next
            n = DoubleNode(curr.val)
            s.next = n
            s = n
        
        prev = nh
        next = prev.next
        while next:
            next.prev = prev
            prev = next
            next = prev.next
        return nh

    def solve(self, A):
        newhead = self.convertDouble(A)
        maxc = 1
        temp = newhead
        while temp:
            #print("temp ",temp.val, " prev ",temp.prev," next ",temp.next)
            if temp.next and temp.val == temp.next.val:
                c, ls, rs = 2, temp, temp.next
                while ls.prev and rs.next and ls.prev.val == rs.next.val:
                    c+=2
                    ls = ls.prev
                    rs = rs.next
                maxc = max(c, maxc)
            if temp.prev and temp.next and (temp.prev.val == temp.next.val):
                #print("here ")
                c, ls, rs = 1, temp, temp
                while ls.prev and rs.next and ls.prev.val == rs.next.val:
                    c+=2
                    ls = ls.prev
                    rs = rs.next
                maxc = max(c, maxc)
           
            temp = temp.next
        return maxc



a = ListNode(2)
b = ListNode(3)
c = ListNode(3)
d = ListNode(3)
e = ListNode(3)
f = ListNode(2)
g = ListNode(1)
a.next = b
b.next = c
c.next = d
#d.next = e
e.next = f
f.next = g

t = Solution()
ans = t.solve(a)
print(ans)