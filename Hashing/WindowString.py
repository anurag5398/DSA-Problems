"""
Given a string A and a string B, find the window with minimum length in A which will contain all the characters in B in linear time complexity.
Note that when the count of a character c in B is x, then the count of c in minimum window in A should be at least x.
Note:
If there is no such window in A that covers all characters in B, return the empty string.
If there are multiple such windows, return the first occurring minimum window ( with minimum start index )
"""

def dictadd(value, tempdict):
    if value in tempdict:
        tempdict[value]+=1
    else:
        tempdict[value] = 1

def dictremove(value, tempdict):
    if value in tempdict:
        tempdict[value]-=1

class Solution2:
    def check(self, i, j):
        for key in self.pattern.keys():
            if key not in self.string:
                self.flag = False
                return
            if self.string[key] < self.pattern[key]:
                self.flag = False
                return
        self.flag = True
        if (j-i) < self.minval:
            self.minval = j-i
            self.ival, self.jval = i, j
        #print(i,j)
        return


    def minWindow(self, A, B):
        self.pattern = dict()
        for i in B:
            dictadd(i, self.pattern)
        self.minval, self.ival, self.jval = 999999, -1, -1

        self.string = dict()
        i, j, self.flag = 0, -1, False
        while True:
            if self.flag is False:
                while self.flag is False:
                    j+=1
                    if j == len(A):
                        if self.jval == -1:
                            return ""
                        else:
                            return A[self.ival:self.jval+1]
                    if A[j] in B:
                        dictadd(A[j], self.string)
                        self.check(i, j)
            else:
                dictremove(A[i], self.string)
                i+=1
                while A[i] not in B:
                    i+=1
                    if i == len(A):
                        if self.jval == -1:
                            return ""
                        else:
                            return A[self.ival:self.jval+1]
                self.check(i, j)


from collections import defaultdict
class Solution:
    def check(self, dict1: defaultdict, dict2: defaultdict) -> bool:
        for k, v in dict1.items():
            if dict2[k] < v: return False
        return True

    #@param A: str
    #@param B: str
    #@return str
    def minWindow(self, A: str, B: str) -> str:
        pattern = defaultdict(int)
        for c in B:
            pattern[c]+=1
        print(pattern)
        word = defaultdict(int)
        setFlag = False
        i, j = -1, -1
        while j + 1 < len(A) and i + 1 < len(A):
            if setFlag is False:
                j+=1
                if A[j] in pattern:
                    word[A[j]]+=1
                    if self.check(pattern, word): 
                        print(i, j)
                        setFlag = True
            else:
                i+=1
                if A[i] in pattern:
                    word[A[i]]-=1
                    if self.check(pattern, word):
                        print(i, j)
                    else:
                        setFlag = False


        

A = "ADOBECODEBANC"
B = "ABC"
test = Solution()
print(test.minWindow(A, B))

