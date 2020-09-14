"""
Given a list containing head pointers of N sorted linked lists. Merge these N given sorted linked lists and return it as one sorted list.
"""
#used heap to select smallest value

import heapq
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Node:
    def __init__(self, ll):
        self.val = ll.val
        self.next = ll.next
    def __lt__(self, other):
        return self.val <= other.val

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        heap = []
        for each in A:
            heapq.heappush(heap, Node(each))
        n = heapq.heappop(heap)
        new_head = ListNode(n.val)
        temp = new_head
        if n.next:
            heapq.heappush(heap, Node(n.next))
        
        while heap:
            n = heapq.heappop(heap)
            temp.next = ListNode(n.val)
            temp = temp.next
            if n.next:
                heapq.heappush(heap, Node(n.next))
        
        return new_head




