class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        i, count = 0, 0
        while i < len(A):
            
            if i != A[i]:
                while i != A[i]:
                    print(A)
                    t1, t2 = A[i], A[A[i]]
                    A[A[i]] = t1
                    A[i] = t2
                    
                    count+=1
            else:
                i+=1
        print(A, count)
a = Solution()
a.solve([1,2,3,4,0])
