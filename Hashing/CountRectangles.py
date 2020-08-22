"""
Given two arrays of integers A and B of size N each, where each pair (A[i], B[i]) for 0 <= i < N represents a unique point (x, y) in 2-D Cartesian plane.
Find and return the number of unordered quadruplet (i, j, k, l) such that (A[i], B[i]), (A[j], B[j]), (A[k], B[k]) and (A[l], B[l]) form a rectangle with the rectangle having all the sides parallel to either x-axis or y-axis.
"""
#for every 2 diagonal points. Check if other 2 points exists. (check if 2 of the 4 poimts don't repeat in different order)
class Solution:
    def solve(self, A, B):
        points = set()
        for x,y in zip(A, B):
            points.add((x,y))
        
        count = 0
        for p1 in range(len(A)):
            for p2 in range(len(A)):
                if A[p2] > A[p1] and B[p2] > B[p1]:
                    p3, p4 = (A[p1], B[p2]), (A[p2], B[p1])
                    if p3 in points and p4 in points:
                        count+=1
        return count

A = [1, 1, 2, 2]
B = [1, 2, 1, 2]
a = Solution()
print(a.solve(A, B))