"""
The local ship renting service has a special rate plan:
It is up to a passenger to choose a ship.
If the chosen ship has X (X > 0) vacant places at the given moment, then the ticket for such a ship costs X.
The passengers buy tickets in turn, the first person in the queue goes first, then goes the second one, and so on up to A-th person.
You need to tell the maximum and the minimum money that the ship company can earn if all A passengers buy tickets.
"""
import heapq
class Solution:
    #@param A : int -> number of passenger
    #@param B : int -> number of ships
    #@param C : list of int -> vacant seats in ships
    #@return list of int -> [maxcost , mincost]
    def solve(self,A ,B, C):
        maxheap = [-i for i in C]
        maxcost = 0
        heapq.heapify(maxheap)

        for i in range(A):
            cost = heapq.heappop(maxheap)
            maxcost+= -cost
            if cost < -1:
                heapq.heappush(maxheap, cost+1)

        mincost = 0
        heapq.heapify(C)

        for i in range(A):
            cost = heapq.heappop(C)
            mincost+= cost
            if cost > 1:
                heapq.heappush(C, cost-1)

        return [maxcost, mincost]

t = Solution()
C = [2,1,1]
print(t.solve(4, 3, C))
