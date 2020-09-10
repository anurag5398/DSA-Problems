"""
Given an array with non negative numbers, divide the array into two parts such that the average of both the parts is equal. Return both parts (If exist). If there is no solution. return an empty list.
NOTE 1: If a solution exists, you should return a list of exactly 2 lists of integers A and B which follow the following condition : numElements in A <= numElements in B
If numElements in A = numElements in B, then A is lexicographically smaller than B ( https://en.wikipedia.org/wiki/Lexicographical_order )
NOTE 2: If multiple solutions exist, return the solution where length(A) is minimum. If there is still a tie, return the one where A is lexicographically smallest.
NOTE 3: Array will contain only non negative numbers.
"""

class Solution:
    def findarray(self, dp, A, i, j):
        ans = []
        popped = []
        while j > 0:
            ans.append(A[i - 1])
            popped.append(i - 1)
            while dp[i - 1][j] is True:
                i-=1
            j-= A[i - 1]
            i-=1
        print(ans)
        return len(ans)
        
            

    def solve(self, A):
        A = sorted(A)
        n = len(A)
        avg = sum(A)//n
        totalSum = avg * (n//2)
        dp = [[False for _ in range(totalSum + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True
        
        for i in range(1, n + 1):
            for j in range(1, totalSum + 1):
                dp[i][j] = dp[i - 1][j]
                if j - A[i-1] >= 0:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - A[i-1]]
        
        
        for avgindex in range(1, n//2):
            tempsum = avg*avgindex
            print(tempsum, avg, avgindex)
            for i in range(n + 1):
                if dp[i][tempsum] is True:
                    l = self.findarray(dp, A, i, tempsum)
                    if l == avgindex:
                        print("found",l)
            else: continue
            break
        



A = [1, 7, 15, 29, 11, 9]
t = Solution()
print(t.solve(A))