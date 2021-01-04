# 行列同士の計算プログラム
n, m, l = map(int, input().split())
a = []
b = []
for _ in range(n):
    c = list(map(int ,input().split()))
    a.append(c)
for _ in range(m):
    d = list(map(int, input().split()))
    b.append(d)
for i in range(n):
    s = ''
    for j in range(l):
        sum = 0
        for k in range(m):
            sum += a[i][k]*b[k][j]
        if j == l-1:
            s += str(sum)
        else:
            s += str(sum)+' '
    print(s)
