"""
Given two array of integers A and B describing a pair of (A[i], B[i]) coordinates in 2D plane. A[i] describe x coordinates of the ith point in 2D plane whereas B[i] describes the y-coordinate of the ith point in 2D plane.

Find and return the maximum number of points which lie on the same line
"""

#missed point : if point overlaps, it will be added to all slopes
A = [ 48,  45, -3,  7, -25, 38,   2,  13, 13, 18, -44, 34, -27, -46,  48, -39, -41, -32, -16, 17, -6, 44, -28, -44, -6, -43, -16, 30, -3, -27, 32, 38, -26, 20, 4, -44, -37 ]
B = [ 47, -42, 41, 22, -4, -35, -45, -22, 5, -20, 21, -13, 47,   32, -48,  47, 17, -23,   30, -30, 37, 42, 44,  23, 1, -40, -9,   34, -34, 49, 16, -35,  2, -19, 31, 23, -37 ]

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def dictadd(key, tempdict):
    if key in tempdict:
        tempdict[key]+=1
    else:
        tempdict[key] = 1

def solve(A, B):
    maxpoints = 0
    for x1, y1 in zip(A, B):
        #print("current point ({},{})".format(x1,y1))
        points = dict()
        points[(0,0)] = -1
        for x2, y2 in zip(A, B):
            m1, m2 = y2-y1, x2-x1
            if m1 == 0 and m2 != 0:
                m2 = -9999
            elif m2 == 0 and m1 != 0:
                m1 = -9999
            elif m1 == 0 and m2 == 0:
                m1 , m2 = m1, m2
            else:
                temp = gcd(m1, m2)
                m1, m2 = m1//temp, m2//temp
            m = (m1, m2)
            dictadd(m, points)
        #print(points,"\n")
        testvalue = max(points.values())+1 + (points[(0,0)] > 0) * points[(0,0)]
        maxpoints = max(testvalue, maxpoints)
    return maxpoints

print(solve(A, B))

