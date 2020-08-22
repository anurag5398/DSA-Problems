import heapq

class Solution:
    def mergeKLists(self, A):
        heap = []
        for each in A:
            heapq.heappush(heap, (each.val, each))
        head = heap[0]
        temp = None
        new = None
        while heap:
            new = heapq.heappop(heap)
            if temp:
                temp[1].next = new[1]
            if new[1].next:
                heapq.heappush(heap, (new[1].next.val , new[1].next))
            temp = new
        return head



from collections import deque 
