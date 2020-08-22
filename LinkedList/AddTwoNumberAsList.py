"""
You are given two linked lists, A and B representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def addTwoNumbers(self, A, B):
        temp1, countA = A, 0
        while temp1:
            countA+=1
            temp1 = temp1.next
        
        temp2, countB = B, 0
        while temp2:
            countB+=1
            temp2 = temp2.next
        
        if countA >= countB:
            a, b = A, B
        else:
            a, b = B, A

        carry = False
        while a or b:
            aval, bval = 0, 0
            if a: aval = a.val
            if b: bval = b.val

            temp = aval+bval+carry
            carry = False
            if temp > 9:
                carry = True
                temp = temp%10
            a.val = temp
            if a: a = a.next
            if b: b = b.next

        if carry:
            node = ListNode(1)
            if countA >= countB:
                a = A
            else:
                a = B
            while a.next:
                a = a.next
            a.next = node

        return A if countA >= countB else B


a = ListNode(5)
b = ListNode(6)
c = ListNode(7)
d = ListNode(8)
e = ListNode(9)
f = ListNode(9)        

a.next = b
b.next = c
c.next = d

e.next = f

t = Solution()
ans  = t.addTwoNumbers(a, e)
while ans:
    print(ans.val)
    ans = ans.next