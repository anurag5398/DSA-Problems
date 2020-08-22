"""
Given a 2D binary matrix of integers A containing 0's and 1's of size N x M.
Find the largest rectangle containing only 1's and return its area.
Note: Rows are numbered from top to bottom and columns are numbered from left to right.
"""
class Stack:
    def __init__(self):
        self.stack = []
        self.count = -1
    def push(self, val):
        self.count+=1
        self.stack.append(val)
    def pop(self):
        if self.count > -1:
            self.count-=1
            return self.stack.pop()
        else:
            return None
    def top(self):
        if self.count > -1:
            return self.stack[self.count]
        else:
            return None

class Solution:
    def maxarea(self, array, size):
        leftstack, rightstack = Stack(), Stack()
        right, left = [None]*size, [None]*size
        for i in range(size):
            while leftstack.count > -1 and array[leftstack.top()]  >= array[i]:
                leftstack.pop()
            if leftstack.count == -1:
                left[i] = -1
            elif array[leftstack.top()] < array[i]:
                left[i] = leftstack.top()
            leftstack.push(i)

            j = size-i-1
            while rightstack.count > -1 and array[rightstack.top()] >= array[j]:
                rightstack.pop()
            if rightstack.count == -1:
                right[j] = size
            elif array[rightstack.top()] < array[j]:
                right[j] = rightstack.top()
            rightstack.push(j)
        
        ans = 0
        for i, val in enumerate(array):
            if val != 0:
                ans = max(val*(right[i]-left[i]-1), ans)
        #print("for array {} maxans {} left{} right {}".format(array, ans, left, right))
        return ans

    def solve(self, A):
        ans = 0
        N, M = len(A), len(A[0])
        for i in range(N):
            if i == 0:
                prev = A[i]
            else:
                for j in range(M):
                    if A[i][j] == 0:
                        prev[j] = 0
                    else:
                        prev[j]+=1
            ans = max(self.maxarea(prev, M), ans)
        return ans


array = [
  [0, 1, 1],
  [1, 0, 0],
  [1, 0, 0],
  [1, 0, 0],
  [1, 0, 0],
  [1, 1, 1],
  [0, 1, 0]
]
test = Solution()
#print(test.maxarea( [1,0, 0], 3 ))
print(test.solve(array))