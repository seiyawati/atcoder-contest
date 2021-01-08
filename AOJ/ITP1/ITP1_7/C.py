r, c = map(int, input().split())
L = []
for i in range(r):
    l = list(map(int, input().split()))
    l.append(sum(l))
    L.append(l)
L.append([])
for j in range(c+1):
    sum = 0
    for k in range(r):
        sum += L[k][j]
    L[-1].append(sum)
for n in range(r+1):
    print(' '.join(map(str, L[n])))