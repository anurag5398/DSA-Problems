"""
Given an array with non negative numbers, divide the array into two parts such that the average of both the parts is equal. Return both parts (If exist). If there is no solution. return an empty list.
NOTE 1: If a solution exists, you should return a list of exactly 2 lists of integers A and B which follow the following condition : numElements in A <= numElements in B
If numElements in A = numElements in B, then A is lexicographically smaller than B ( https://en.wikipedia.org/wiki/Lexicographical_order )
NOTE 2: If multiple solutions exist, return the solution where length(A) is minimum. If there is still a tie, return the one where A is lexicographically smallest.
NOTE 3: Array will contain only non negative numbers.
"""

class Solution:
    def findsubset(self, reqSum, length):
        dp = [[False for _ in range(reqSum + 1)] for _ in range(self.n + 1)]
        parent = [[(-1, -1) for _ in range(reqSum + 1)] for _ in range(self.n + 1)]
        for i in range(self.n + 1):
            dp[i][0] = True

        for i in range(1, self.n + 1):
            for j in range(1, reqSum + 1):
                dp[i][j] = dp[i-1][j] or dp[i-1][j-self.A[i-1]]
        print(dp)
            

    def solve(self, A):
        total = 0
        self.n = len(A)
        self.A = A
        for i in A:
            total+=i
        avg = total/self.n
        if int(avg) != avg: return []

        for length in range(self.n//2):
            reqSum = avg * length
            self.findsubset(reqSum, length)



A = [1, 7, 15, 29, 11, 9]
t = Solution()
print(t.solve(A))