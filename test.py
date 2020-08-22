A = [19, 10, 12, 10, 24, 25, 22]

uni = list()

for i in range(len(A)):
    for j in range(i+1, len(A)):
        if (A[i]+A[j])%4 == 0:
            uni.append((A[i], A[j]))

#print(uni)


def solve(i, indexList, cant):
    if i == len(indexList):
        print(cant)
        return
    first = indexList[i][0]
    second = indexList[i][1]
    if first not in cant:
        cant.add(first)
        solve(i+1, indexList, cant)
        cant.remove(first)
    if second not in cant:
        cant.add(second)
    solve(i+1, indexList, cant)
    

solve(0, uni, set())

t = {'b':[],'c':[2,5]}
f = {'c':[2],'b':[]}
print(len(t))