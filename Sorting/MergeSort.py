class Solution:
    # @param A : list of integers
    # @return a list of integers
    def merge(self, l, m, r, A):
        temp1 = [A[i] for i in range(l, m+1)]
        temp2 = [A[i] for i in range(m+1, r+1)]
        i, j = 0, 0
        index = l
        while i < len(temp1) and j < len(temp2):
            if temp1[i] <= temp2[j]:
                A[index] = temp1[i]
                i+=1
            else:
                A[index] = temp2[j]
                j+=1
            index+=1
        while i < len(temp1):
            A[index] = temp1[i]
            i+=1
            index+=1
        while j < len(temp2):
            A[index] = temp2[j]
            j+=1
            index+=1
        
    def mergesort(self, l, r, A):
        if l >= r:
            return
        m = l + (r-l)//2
        self.mergesort(l, m, A)
        self.mergesort(m+1, r, A)
        self.merge(l, m, r, A)