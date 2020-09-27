"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
Given an array of words A of size N written in the alien language, and the order of the alphabet denoted by string B of size 26, return 1 if and only if the given words are sorted lexicographicaly in this alien language else return 0.
"""

class Solution:
    #@param word1, word2: str
    #@param pos: dict
    #@return bool
    def compare(self, word1, word2, pos):
        len1, len2 = len(word1), len(word2)
        for i in range(min(len1, len2)):
            if pos[word1[i]] > pos[word2[i]]: return False
            if pos[word1[i]] < pos[word2[i]]: return True
        if len2 < len1: return False
        return True

    #@param A: list of str
    #@param B: str
    #@return int
    def solve(self, A: list, B: str) -> int:
        pos = dict()
        for i, v in enumerate(B):
            pos[v] = i
        
        for i in range(len(A) - 1):
            if self.compare(A[i], A[i+1], pos) is False:
                return 0
        return 1



A = ["fine", "none", "no"]
B = "qwertyuiopasdfghjklzxcvbnm"
t = Solution()
print(t.solve(A, B))