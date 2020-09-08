"""
There is a rod of length A lying on x-axis with its left end at x = 0 and right end at x = A. Now, there are M weak points on this rod denoted by positive integer values(all less than A) B1, B2, ..., BM.
You have to cut rod at all these weak points. You can perform these cuts in any order.
After a cut, rod gets divided into two smaller sub-rods. Cost of making a cut is the length of the sub-rod in which you are making a cut.
Your aim is to minimise this cost. Return an array denoting the sequence in which you will make cuts. If two different sequences of cuts give same cost, return the lexicographically smallest.
NOTE: Sequence a1, a2 ,..., an is lexicographically smaller than b1, b2 ,..., bm, if and only if at the first i where ai and bi differ, ai < bi, or if no such i found, then n < m.
"""
#First semi-problem is to find the minimum cost after cutting all joints
#for each join in between(k) cost will be  dp[i][j] = dp[i][k] + dp[k][j] + (j-i)
#so for all lengths we will select the minimum value of all partitions
#in dp matrix ith represents starting of rod and jth represents end of rod

#Second problem is to fint he order of cuts
#We can create a parent matrix and fill simultaneously with dp, the cut for
#which we are selecting value i.e minimum value cut between any two point

#finally we will create a queue and all (start, end)
#we will pop this out find the selected cut for this range, and append the 
#new formed sections, eg. (0-6) parent[0][6] then appendleft [0][parent] and [parent][6] in our queue
#this will happen until all cuts are accounted i.e all parent are now 0


from collections import deque
class Solution:
    #@param A : int
    #@param B : list of int
    #@return list of int
    def solve(self, A, B):
        B.insert(0,0)
        B.append(A)
        l = len(B)
        dp = [[0 for _ in range(l)] for _ in range(l)]
        parent = [[0 for _ in range(l)] for _ in range(l)]
        

        for k in range(2, l):
            for i in range(0, l-k):
                j = i + k
                dp[i][j] = float('inf')
                for z in range(i+1, j):
                    temp = dp[i][z] + dp[z][j] + (B[j]-B[i])
                    if temp < dp[i][j]:
                        dp[i][j] = temp
                        parent[i][j] = z
                    elif temp == dp[i][j]:
                        if z < parent[i][j]:
                            parent[i][j] = z
        q = deque()
        q.append((0, l-1))
        ans = []
        while q:
            #print(q)
            s, e = q.popleft()
            temp = parent[s][e]
            if temp == 0: continue
            ans.append(B[temp])
            q.appendleft((temp, e))
            q.appendleft((s, temp))
        return ans
                        



A = 7
B = [1, 2, 3, 6]
t = Solution()
print(t.solve(A, B))