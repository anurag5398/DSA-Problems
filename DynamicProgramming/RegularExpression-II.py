"""
Implement wildcard pattern matching with support for ' ? ' and ' * ' for strings A and B.

' . ' : Matches any single character.
' * ' : Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
"""

class Solution:
    #@param A : string
    #@param B : string -> pattern
    #@return 1 or 0
    def isMatch(self, A, B):
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
        for i in range(1, len(B)+1):
            if B[i-1] == '*':
                prev[i] = prev[i-2]

        curr = [False] * (len(B)+1)

        for i in range(1, len(A)+1):
            if i != 1:
                prev = curr
                curr = [False] * (len(B)+1)
            for j in range(1, len(B)+1):
                if A[i-1] == B[j-1] or B[j-1] == '.':
                    curr[j] = prev[j-1]
                elif B[j-1] == '*':
                    if A[i-1] == B[j-2] or B[j-2] == '.':
                        curr[j] = curr[j-1] | prev[j]
                    else:
                        curr[j] = curr[j-2]
        return 1 if curr[j] else 0


t = Solution()
A = "hshhsggcgk"
B = ".*************u**"
print(t.isMatch(A, B))
            