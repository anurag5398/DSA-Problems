"""
Given an array A of length N. You have to answer Q queires.
Each query will contain 4 integers l1, r1, l2 and r2. If sorted segment from [l1, r1] is same as sorted segment from [l2 r2] then answer is 1 else 0.
NOTE The queries are 0-indexed.
"""
import random

class Solution:
    def solve(self, A, B):
        mapvalues, values = dict(), set()
        for i, val in enumerate(A):
            if val in mapvalues:
                A[i] = mapvalues[val]
            else:
                temp = random.randint(10**2,10**18)
                while temp in values:
                    temp = random.randint(10**2,10**18)
                values.add(temp)
                mapvalues[val] = temp
                A[i] = temp
        #print(A)

        current = 0
        for i, val in enumerate(A):
            current+= val
            A[i] = current
        #print(A)

        ans = []
        for s1,e1,s2,e2 in B:
            if s1 == 0:
                temp1 = A[e1]
            else:
                temp1 = A[e1] - A[s1-1]
            
            if s2 == 0:
                temp2 = A[e2]
            else:
                temp2 = A[e2] - A[s2-1]

            if temp1 == temp2:
                ans.append(1)
            else:
                ans.append(0)
        return ans
a = Solution()
A = [1,7,11,8,11,7,1]
B = [
    [0,2,4,6],
    [1,2,4,5],
    [0,0,0,0],
    [1,6,1,6]
]
a.solve(A, B)