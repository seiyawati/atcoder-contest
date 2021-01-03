n, m = map(int, input().split())
arr1 = []
arr2 = []
for _ in range(n):
    retu = list(map(int, input().split()))
    arr1.append(retu)
for _ in range(m):
    tate = int(input())
    arr2.append(tate)
for i in range(n):
    count = 0
    for j in range(m):
        count += arr1[i][j]*arr2[j]
    print(count)