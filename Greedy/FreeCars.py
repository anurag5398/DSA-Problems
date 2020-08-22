"""
Given two arrays A and B of size N. A[i] represents the time by which you can buy ith car without paying any money.
B[i] represents the profit you can earn by buying ith car. It takes 1 minute to buy a car so, you can only buy the ith car when the current time <= A[i] - 1.
Your task is to find maximum profit one can earn by buying cars considering that you can only buy one car at a time.
"""
import heapq

class Solution:
    #A time B profit
    def solve(self, A, B):
        heap = []
        value = tuple(zip(A, B))
        value = sorted(value)
        time = 0
        for t,p in value:
            if time < t:
                heapq.heappush(heap, p)
                time+=1
            else:
                if heap[0] < p:
                    heapq.heappushpop(heap, p)
        return sum(heap)



t = Solution()
A = [ 1, 7, 6, 2, 8, 4, 4, 6, 8, 2 ]
B = [ 8, 11, 7, 7, 10, 8, 7, 5, 4, 9 ]
print(t.solve(A, B))