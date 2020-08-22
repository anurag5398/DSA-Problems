"""
Max Heap is a special kind of complete binary tree in which for every node the value present in that node is greater than the value present in it’s children nodes.
Find the number of distinct Max Heap can be made from A distinct integers.
In short, you have to ensure the following properties for the max heap :
Heap has to be a complete binary tree ( A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.)
Every node is greater than all its children.
NOTE: If you want to know more about Heaps, please visit this link. Return your answer modulo 109 + 7.
"""
#incomplete
import math
class Solution:
    def fact(self, no):
        no = int(no)
        if no == 1 or no == 0: return 1
        temp = 1
        for i in range(2, no+1):
            temp*= i
        return temp

    def combi(self, n, r):
        return self.fact(n)//(self.fact(r)*self.fact(n-r))

    def solve(self, A):
        print(A)
        h = math.log2(A)
        x = (2**h)-1
        l = (x-2 )/2 + min(A-x, (x+1)/2)
        r = (A-1)-l
        nodes = self.combi(A-1,l)*self.solve(l)*self.solve(r)
        return nodes

t = Solution()
print(t.solve(4))