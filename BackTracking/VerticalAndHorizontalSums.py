"""
Given a matrix B, of size N x M, you are allowed to do at most A special operations on this grid such that there is no vertical or horizontal contiguous subarray that has a sum greater than C.
A special operation involves multiplying any element by -1 i.e. changing its sign.
Return 1 if it is possible to achieve the answer, otherwise 0.
"""
#TLE solution
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @return an integer
    
    #for max sum subarray
    def kadanes(self, array, size):
        maxsum, ans = 0, array[0]
        for i in range(size):
            if maxsum+array[i] > array[i]:
                maxsum+= array[i]
            else:
                maxsum = array[i]
            ans = max(maxsum, ans)
        return ans
            
    
    #check all arrays i's and j's    
    def fullcheck(self, B):
        for index in range(self.ilength):
            temp = self.kadanes([B[index][temp] for temp in range(self.jlength)], self.jlength)
            if temp > self.maxval:
                return False
        for index in range(self.jlength):
            temp = self.kadanes([B[temp][index] for temp in range(self.ilength)], self.ilength)
            if temp > self.maxval:
                return False
        return True
    
    #check initially safe i and j    
    def precheck(self, B):
        for index in range(self.ilength):
            temp = self.kadanes([B[index][temp] for temp in range(self.jlength)], self.jlength)
            if temp <= self.maxval:
                self.iset.add(index)
        for index in range(self.jlength):
            temp = self.kadanes([B[temp][index] for temp in range(self.ilength)], self.ilength)
            if temp <= self.maxval:
                self.jset.add(index)
        
        
                
    #recursion -> -ve or +ve
    def sums(self, i, j, moves, B):
        if self.ans:
            return
        if moves < 0:
            return
        if j == self.jlength:
            self.sums(i+1, 0, moves, B)
            return
        if i == self.ilength:
            if self.fullcheck(B):
                #print("found match B {} moves {}".format(B, moves))
                self.ans = True
            return
        #if self.positioninvalid(i, j, B):
        if i not in self.iset or j not in self.jset:
            B[i][j] = -B[i][j]
            self.sums(i, j+1, moves-1, B)
            B[i][j] = -B[i][j]
        self.sums(i, j+1, moves, B)
        
        
    
    def solve(self, A, B, C):
        
        self.ans = False
        self.ilength, self.jlength = len(B), len(B[0])
        self.maxval = C
        
        self.iset, self.jset = set(), set()
        self.precheck(B)
        
        self.sums(0, 0, A, B)
        return 1 if self.ans else 0
