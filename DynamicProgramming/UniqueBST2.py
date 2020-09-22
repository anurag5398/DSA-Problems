"""
Given an integer A, how many structurally unique BST's (binary search trees) exist that can store values 1...A?
"""
#observation: value of node dosent matter in BST, just number of node
#any node can act as root
#CATALAN NUMBER

class Solution:
    #@param A : int -> number of nodes
    #@return int -> total nodes/catalan number of A
    def numTrees(self, A):
        dp = [0] * (A+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, A+1):
            for j in range(i):
                dp[i]+= ( dp[j] * dp[i-1-j] )
        return dp[A]

t = Solution()
print(t.numTrees(2))