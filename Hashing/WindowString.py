"""
Given a string A and a string B, find the window with minimum length in A which will contain all the characters in B in linear time complexity.
Note that when the count of a character c in B is x, then the count of c in minimum window in A should be at least x.
Note:
If there is no such window in A that covers all characters in B, return the empty string.
If there are multiple such windows, return the first occurring minimum window ( with minimum start index )
"""

from collections import defaultdict

class Solution:
    #@param string : string
    #@param i, j : int
    def formans(self, string, i, j):
        if (j - i) < self.minans:
            self.minans = j - i
            self.ans = string
        
    #@param A : string
    #@param B : string
    #@return string
    def minWindow(self, A, B):
        if len(B) == 0: return ""
        if len(B) == 1:
            if B in A: return B
            else: return ""
        Bchar = defaultdict(int)
        for i in B:
            Bchar[i]+=1
        self.ans = ""
        self.minans = float('inf')
        completed = set()
        lenBchar = len(Bchar)
        lenCompleted = 0
        Achar = defaultdict(int)
        i, j = 0, 0
        Achar[A[0]]+=1
        n = len(A)
        while i < n and j < n:
            if lenCompleted == lenBchar:
                self.formans(A[i:j+1], i, j)
                remove = A[i]
                i+=1
                if remove in Bchar:
                    Achar[remove]-=1
                    if Achar[remove] < Bchar[remove]:
                        completed.remove(remove)
                        lenCompleted-=1
            else:
                j+=1
                if j < n:
                    addele = A[j]
                    if addele in Bchar:
                        Achar[addele]+=1
                        if Achar[addele] >= Bchar[addele] and addele not in completed:
                            completed.add(addele)
                            lenCompleted+=1
        if lenCompleted == lenBchar:
            self.formans(A[i:j+1], i, j)
        return self.ans
                            
                            
        
            
        



        

A = "ADOBECODEBANC"
B = "ABC"
test = Solution()
print(test.minWindow(A, B))

