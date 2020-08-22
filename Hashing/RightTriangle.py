"""
Given two arrays of integers A and B of size N each, where each pair (A[i], B[i]) for 0 <= i < N represents a unique point (x, y) in 2D Cartesian plane.
Find and return the number of unordered triplets (i, j, k) such that (A[i], B[i]), (A[j], B[j]) and (A[k], B[k]) form a right angled triangle with the triangle having one side parallel to the x-axis and one side parallel to the y-axis.
NOTE: The answer may be large so return the answer modulo (109 + 7).
"""
#for each point, total right triangle is:  (horizontal points)*(vertical points)

class Solution:
    def adddict(self, val, tempdict):
        if val in tempdict:
            tempdict[val]+=1
        else:
            tempdict[val] = 1

    def solve(self, A, B):
        xfreq, yfreq = dict(), dict()
        for i, j in zip(A, B):
            self.adddict(i, xfreq)
            self.adddict(j, yfreq)
        
        totalpoints = 0
        for x, y in zip(A, B):
            totalpoints+= (xfreq[x]-1)*(yfreq[y]-1)
        
        return totalpoints


A = [0,1,1]
B = [0,1,1]
a = Solution()
print(a.solve(A, B))