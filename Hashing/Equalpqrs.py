"""
Given an array A of N integers, find the index of values that satisfy P + Q = R + S, where P,Q,R & S are integers values in the array
S1 is lexicographically smaller than S2 if:
  A1 < A2 OR
  A1 = A2 AND B1 < B2 OR
  A1 = A2 AND B1 = B2 AND C1 < C2 OR 
  A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2
"""
class Solution:
    def equal(self, A):
        sumdict = dict()
        size = len(A)
        ans = [9999,9999,9999,9999]
        for i in range(size):
            for j in range(i+1, size):
                val = A[i]+A[j]
                if val in sumdict:
                    if sumdict[val][0] != i and sumdict[val][1] != i and sumdict[val][0] != j and sumdict[val][1] != j:
                        tempans = [sumdict[val][0], sumdict[val][1], i, j]
                        ans = min(tempans, ans)
                else:
                    sumdict[val] = (i, j)
        return ans
                        

        
     

a = Solution()
A = [2, 5, 1, 6]
print(a.equal(A))