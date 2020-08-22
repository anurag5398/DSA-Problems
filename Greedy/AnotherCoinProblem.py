"""
The monetary system in DarkLand is really simple and systematic. The locals only use coins. The coins come in different values. The values used are:
 1, 5, 25, 125, 625, 3125, 15625, ...
Formally, for each K >= 0 there are coins worth 5K.
Given an integer A denoting the cost of an item, find and return the smallest number of coins necessary to pay exactly the cost of the item (assuming you have a sufficient supply of coins of each of the types you will need).
"""
import math
class Solution:
    #@param A : int
    #@return int
    def solve(self, A):
        coins = 0
        while A > 0:
            p = math.log(A, 5)
            A = A - 5**int(p)
            coins+=1
        return coins

t = Solution()
print(t.solve(9))
        