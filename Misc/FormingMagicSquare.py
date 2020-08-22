"""
We define a magic square to be an  matrix of distinct positive integers from  to  where the sum of any row, column, or diagonal of length  is always equal to the same number: the magic constant.
You will be given a  matrix  of integers in the inclusive range . We can convert any digit  to any other digit  in the range  at cost of . Given , convert it into a magic square at minimal cost. Print this cost on a new line.
Note: The resulting magic square must contain distinct integers in the inclusive range .
"""
#Valid of 3X3
#only 8 possible magic squares of 8X8


#@param matrix : list of list of int
#@return list of list of int -> mirror image of matrix
def mirrorOfMatrix(matrix):
    n, m = len(matrix), len(matrix[0])
    newMatrix = [[0 for i in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            newMatrix[i][j] = matrix[i][m-j-1]
    return newMatrix

#@param matrix : list of list of int
#@return list of list of int : right roatated
def rightRotate(matrix):
    n, m = len(matrix), len(matrix[0])
    newMatrix = [[0 for i in range(m)] for i in range(n)]
    for j in range(m):
        for i in range(n):
            newMatrix[i][j] = matrix[n-j-1][i]
    return newMatrix

#@param m1, m2 : list of list of int
#@return int -> diff in each cell
def differenceInMatrix(m1, m2):
    cost = 0
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            cost+= abs(m1[i][j]-m2[i][j])
    return cost
    



#@param A : list of list of int
#@return int -> min cost
def formingMagicSquare(A):
    base = [
        [4,3,8],
        [9,5,1],
        [2,7,6]
    ]
    mincost = float('inf')
    for i in range(4):
        mirrorbase = mirrorOfMatrix(base)
        mincost = min(differenceInMatrix(A, base), 
                        differenceInMatrix(A, mirrorbase), mincost)
        
        base = rightRotate(base)
    return mincost
    




A = [
    [4,9,2],
    [3,5,7],
    [8,1,5]
]
print(magicsquare(A))

    