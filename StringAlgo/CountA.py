"""
You are given a string A. Find the number of substrings that start and end with 'a'.
"""
class Solution:
    def solve(self, A):
        count = 0
        temp = 1
        for i in A:
            if i == 'a':
                count+=temp
                temp+=1
        return count

t = Solution()
print(t.solve("abababab"))
