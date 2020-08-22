"""
Given character matrix A of O's and X's, where O = white, X = black.
Return the number of black shapes. A black shape consists of one or more adjacent X's (diagonals not included)
"""

class Solution:
    #@param i, j: int
    #@param matric : list of list o
    def mark(self, i, j, matrix):
        matrix[i][j] = '0'
        if i - 1 > -1 and matrix[i - 1][j] == 'X':
            self.mark(i - 1, j, matrix)
        if i + 1 < len(matrix) and matrix[i + 1][j] == 'X':
            self.mark(i + 1, j, matrix)
        if j - 1 > -1 and matrix[i][j - 1] == 'X':
            self.mark(i, j - 1, matrix)
        if j + 1 < len(matrix[0]) and matrix[i][j + 1] == 'X':
            self.mark(i, j + 1, matrix)

    #@param A : list of string
    #@return int
    def solve(self, A):
        matrix = list()
        for i in A: matrix.append(list(i))
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 'X':
                    count+=1
                    self.mark(i, j, matrix)
        return count

t = Solution()
A = [ "X00", "X00", "0XX" ]
print(t.solve(A))