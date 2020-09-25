"""
Rick and Morty are best friends. Rick and Morty will change their name to strings A and B respectively.
They want to know if it is possible to transform A into B by doing zero or more conversions.
In one conversion you can convert all occurrences of one character in A to any other lowercase English character.
"""
"""
Scenarios:
1) Same String
2) All the char in string map to same char (possible to convert by intermediate)
3) One char maps to different char (not possible)
4) All char map to same char but there is no intermediate char available(i.e all 26 input char used in string)
"""

class Solution:
    #@param A: str
    #@param B: str
    #@return bool
    def solve(self, A: str, B: str) -> bool:
        if A == B: return 1
        mapping = dict()
        for i in range(len(A)):
            if A[i] in mapping:
                if mapping[A[i]] != B[i]:
                    return 0
            else:
                mapping[A[i]] = B[i]
        if len(mapping) == 26: return 0
        return 1

t = Solution()
A = "abcab"
B = "abcdb"
print(t.solve(A, B))