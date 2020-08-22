def partition(l, r, A):
        pivot, i = A[r], l-1
        for j in range(l, r):
            if A[j] <= pivot:
                i+=1
                A[i], A[j] = A[j], A[i]
        i+=1
        A[i], A[r] = A[r], A[i]
        return i
    
def quicksort(l, r, A):
    if l < r:
        part = partition(l, r, A)
        quicksort(l, part-1, A)
        quicksort(part+1, r, A)

a = [3,4,2,8,1,5]
quicksort(0, 5, a)
print(a)