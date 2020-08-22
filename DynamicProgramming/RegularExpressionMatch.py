"""
Implement wildcard pattern matching with support for ' ? ' and ' * ' for strings A and B.

' ? ' : Matches any single character.
' * ' : Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
"""
#both solution works, 2nd solution is space and time optimized 


class SolutionAlt:
    #@param A, B : string
    #@return 1 or 0
    def isMatch(self, A, B):
        dp = [[False for i in range(len(B)+1)] for i in range(len(A)+1)]
        dp[0][0] = True

        for j in range(1, len(B)+1):
            if B[j-1] == '*':
                dp[0][j] = True

        for i in range(0, len(A)+1):
            for j in range(1, len(B)+1):

                if i == 0:
                    if B[j-1] == '*':
                        dp[i][j] = dp[i][j-1]
                    else: continue
                
                if A[i-1] == B[j-1] or B[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]

                elif B[j-1] == '*':
                    dp[i][j] = dp[i-1][j] | dp[i][j-1] | dp[i-1][j-1]
                
                else:
                    dp[i][j] = False
            
        return 1 if dp[i][j] else 0

class Solution:
    #@param A : string
    #@param B : string -> pattern
    #@return 1 or 0
    def isMatch(self, A, B):
        #reducing size of B for consecutive *s
        temp = list(B)
        i = 0
        while i < len(temp)-1:
            if temp[i] == '*':
                if temp[i+1] == '*':
                    temp.pop(i+1)
                else: i+=1
            else: i+=1
        
        B = "".join(temp)
        prev = [False] * (len(B)+1)
        prev[0] = True
        
        
        #fill when stringA is empty
        for i in range(1, len(B)+1):
            if B[i-1] == '*':
                prev[i] = prev[i-1]

        curr = [False] * (len(B)+1)
        
        #if any string is empty
        if len(A) == 0:
            return 1 if prev[len(B)] else 0
        if len(B) == 0:
            if len(A) == 0: return 1
            else: return 0

        for i in range(1, len(A)+1):
            if i != 1:
                prev = curr
                curr = [False] * (len(B)+1)
            for j in range(1, len(B)+1):
                if A[i-1] == B[j-1] or B[j-1] == '?':
                    curr[j] = prev[j-1]
                elif B[j-1] == '*':
                    curr[j] = curr[j-1] | prev[j]
            
        return 1 if curr[j] else 0

        

t = Solution()
A = "acz"
B = "a?a"
print(t.isMatch(A, B))
                
