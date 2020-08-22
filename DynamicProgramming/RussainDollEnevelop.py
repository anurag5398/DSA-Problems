"""
Given a matrix of integers A of size N x 2 describing dimensions of N envelopes, where A[i][0] denotes the height of the ith envelope and A[i][1] denotes the width of the ith envelope.
One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.
Find the maximum number of envelopes you can put one inside other.
"""

class Solution:
    #@param l, m, r: int
    def merge(self, l, m, r, A):
        temp1 = [A[i] for i in range(l, m+1)]
        temp2 = [A[i] for i in range(m+1, r+1)]
        index = l
        i, j = 0, 0
        while i < len(temp1) and j < len(temp2):
            if temp1[i][0] < temp2[j][0]:
                A[index] = temp1[i]
                i+=1
            elif temp1[i][0] == temp2[j][0]:
                if temp1[i][1] > temp2[j][1]:
                    A[index] = temp1[i]
                    i+=1
                else: 
                    A[index] = temp2[j]
                    j+=1
            else:
                A[index] = temp2[j]
                j+=1
            index+=1
        
        while i < len(temp1):
            A[index] = temp1[i]
            index+=1
            i+=1
        
        while j < len(temp2):
            A[index] = temp2[j]
            index+=1
            j+=1

    #param l : int
    #@param r: int
    #@param A : list of int
    def mergesort(self, l, r, A):
        if l >= r: return
        m = l + (r-l)//2
        self.mergesort(l, m, A)
        self.mergesort(m+1, r, A)
        self.merge(l, m, r, A)

    #@param A : list of list of int -> N * (height X width)
    #@return int -> maximum number of envelops which can
    #go inside each other
    def solve(self, A):
        self.mergesort(0, len(A)-1, A)
        
        dp = [0] * len(A)
        dp[0] = 1
        maxans = 0
        for i in range(1, len(A)):
            for j in range(i):
                if A[j][1] < A[i][1] and dp[j] > dp[i]:
                    dp[i] = dp[j]
            dp[i]+=1
            maxans = max(dp[i], maxans)
        return maxans

A = [
    [5,6],[6,4],[6,7],[2,3]
]

t = Solution()
print(t.solve(A))
