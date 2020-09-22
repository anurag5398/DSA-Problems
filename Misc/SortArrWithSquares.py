"""
Given a sorted array A containing N integers both positive and negative.
You need to create another array containing the squares of all the elements in A and return it in non-decreasing order.
Try to this in O(N) time.
"""
#positive numbers will have squares in increasing order
#negative numbers will have squares in decreasing order


class Solution:
    #@param A: list of int
    #@return list of int
    def solve(self, A: list) -> list:
        midindex = -1
        for i, v in enumerate(A):
            if v >= 0 and midindex == -1:
                midindex = i
            A[i] = v * v
        if midindex == 0: return A

        j, i = midindex, midindex - 1
        ans = [0 for _ in range(len(A))]
        pos = 0
        while i > -1 and j < len(A):
            if A[i] <= A[j]:
                ans[pos] = A[i]
                i-=1
            else:
                ans[pos] = A[j]
                j+=1
            pos+=1
        while i > -1:
            ans[pos] = A[i]
            i-=1
            pos+=1
        while j < len(A):
            ans[pos] = A[j]
            j+=1
            pos+=1
        return ans

t = Solution()
A = [-6, -3, -1, 2, 4, 5]
print(t.solve(A))
