"""
Given a linked list A, remove the B-th node from the end of list and return its head.
For example, Given linked list: 1->2->3->4->5, and B = 2. After removing the second node from the end, the linked list becomes 1->2->3->5.
NOTE: If B is greater than the size of the list, remove the first node of the list.
NOTE: Try doing it using constant additional space.
"""
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    def removeNthFromEnd(self, A, B):
        j = A
        while B > 0 and j.next != None:
            j = j.next
            B-=1
        
        i = A
        while j.next != None:
            i = i.next
            j = j.next
        if i == A:
            return A.next
        i.next = i.next.next
        return A