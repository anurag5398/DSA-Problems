"""
Given a string A made up of multiple brackets of type "[]" , "()" and "{}" find the length of the longest substring which forms a balanced string .
Conditions for a string to be balanced :
Blank string is balanced ( However blank string will not be provided as a test case ).
If B is balanced : (B) , [B] and {B} are also balanced.
If B1 and B2 are balanced then B1B2 i.e the string formed by concatenating B1 and B2 is also balanced.
"""

# {} -> 0, () -> 1, [] -> 2

#Not Done
class Solution:
    #@param A : string
    #@return int
    def LBSlength(self, A):
        A = '#'+A
        stack = [0]
        maxLength = 0
        for i, s in enumerate(A):
            if s == '(' or s == '[' or s == '{':
                stack.append(i)
            elif s == ')' and A[stack[-1]] == '(':
                stack.pop()
                maxLength = max(i-stack[-1], maxLength)
            elif s == '}' and A[stack[-1]] == '{':
                stack.pop()
                maxLength = max(i-stack[-1], maxLength)
            elif s == ']' and A[stack[-1]] == '[':
                stack.pop()
                maxLength = max(i-stack[-1], maxLength)
            else:
                stack.append(i)
        return maxLength


        


t = Solution()
st = ']['
print(t.LBSlength(st))
                
            
            