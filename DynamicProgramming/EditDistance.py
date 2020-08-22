"""
Given two strings A and B, find the minimum number of steps required to convert A to B. (each operation is counted as 1 step.)
You have the following 3 operations permitted on a word:
Insert a character
Delete a character
Replace a character
"""

class Solution:
    #@param A : string
    #@param B : string
    #@return an int
    def minDistance(self, A, B):
        cost = [[0 for i in range(len(B)+1)] for i in range(len(A)+1)]
        for i in range(len(A)+1):
            for j in range(len(B)+1):
                #string1 empty
                if i == 0:
                    cost[i][j] = j

                #string2 empty
                elif j == 0:
                    cost[i][j] = i

                #same charecter
                elif A[i-1] == B[j-1]:
                    cost[i][j] = cost[i-1][j-1]

                #consider all 3 case
                else:
                    cost[i][j] = 1 + min(
                        cost[i][j-1],    #insert
                        cost[i-1][j],    #delete
                        cost[i-1][j-1]   #replace
                    )
        return cost[i][j]




t = Solution()
a = "abad"
b = "abbc"
print(t.minDistance(a, b))
