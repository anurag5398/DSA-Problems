"""
Given N persons with different priorities standing in a queue.
Queue is following a property that Each person is standing atmost B places away from it's sorted position.
Your task is to sort the queue in the increasing order of priorities.
NOTE:
No two persons can have the same priority.
Use the property of the queue to sort the queue with complexity O(NlogB).
"""
import heapq
class Solution:
    #@param A: list of int
    #@param B : int
    #@return list of int
    def solve(self, A: list, B: int) -> list:
        heap = A[:B + 1]
        heapq.heapify(heap)
        i = B + 1
        pos = 0
        while heap:
            ele = heapq.heappop(heap)
            A[pos] = ele
            if i < len(A):
                heapq.heappush(heap, A[i])
                i+=1
            pos+=1
        return A

t = Solution()
A = [2, 1, 17, 10, 21, 95]
B = 1
print(t.solve(A, B))

    