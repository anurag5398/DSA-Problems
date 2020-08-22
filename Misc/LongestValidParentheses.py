"""
Given a string A containing just the characters '(' and ')'.
Find the length of the longest valid (well-formed) parentheses substring.
"""

class Solution:
    #@param A: string -> (,)
    #@return int -> max valid length
    def longestValidParentheses(self, A):
        stack = [-1]
        size = 0
        for i in range(len(A)):
            if A[i] == '(':
                stack.append(i)
            elif A[i] == ')':
                if stack[-1] != -1 and A[stack[-1]] == '(':
                    stack.pop()
                    size = max(i-stack[-1], size)
                else:
                    stack.append(i)
        return size


t = Solution()
A = "(()))()"
print(t.longestValidParentheses(A))


    