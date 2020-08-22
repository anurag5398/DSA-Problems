string = "xxyaxxya"

def Zalgo(s):
    l, r = 0, 0
    n = len(s)
    z = [None]*n
    z[0] = n
    for i in range(1,n):
        if i > r:
            l, r = i, i
            while r < n and s[r] == s[r-l]: r+=1
            z[i] = r-l
            r-=1
        else:
            if i+z[i-l] <= r: z[i] = z[i-l]
            else:
                l = i
                while r < n and s[r] == s[r-l]: r+=1
                z[i] = r-l
                r-=1
        print(z)

Zalgo("abcabcd")