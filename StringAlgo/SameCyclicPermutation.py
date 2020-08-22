"""
Given two String A, B of same length.
Find the number of cyclic permutations of B that are same as A.
"""
def zAlgo(s):
    l, r = 0, 0
    n = len(s)
    z = [None]*n
    z[0] = n
    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and s[r] == s[r-l]: r+=1
            z[i] = r-l
            r-=1
        else:
            if i + z[i-l] <= r: z[i] = z[i-l]
            else:
                l = i
                while r < n and s[r] == s[r-l]: r+=1
                z[i] = r-l 
                r-=1
    return z

def solve(A, B):
    B = B + B
    B = B[0:-1]
    size = len(A)
    string = A + "#" + B
    temp = zAlgo(string)
    count = 0
    for i, val in enumerate(temp):
        if i == 0:
            continue
        if val >= size: count+=1
    return count

#print(zAlgo("xxyaxxyazxxyaxxyaxz"))
a = solve("aba", "aba")
print(a)