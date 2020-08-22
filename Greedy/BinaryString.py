"""
You are given a string A consisting of 1's and 0's. Now the task is to make the string consisting of only 1's. But you are allowed to perform only the following operation:
Take exactly B consecutive elements of string and change 1 to 0 and 0 to 1.
Each operation takes 1 unit time so you have to determine the minimum time required to make the string of 1's only. If not possible return -1.
"""

class Solution:
    #paramA - binary string
    #paramB - int
    #return -1/count
    def flip(self, n):
        if n == '1': return '0'
        else: return '1'

    def solve(self, A, B):
        k = B
        A = list(A)
        c = 0
        for i in range(0, len(A)-k+1):
            if A[i] == '0':
                c+=1
                for j in range(i,i+k):
                    A[j] = self.flip(A[j])
        
        for i in range(len(A)-k+1, len(A)):
            if A[i] == '0': return -1

        return c

A = "011"
B = 3
t = Solution()
print(t.solve(A, B))
            