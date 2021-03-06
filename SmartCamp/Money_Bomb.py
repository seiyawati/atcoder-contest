n, m, k = map(int, input().split())
room = []

for i in range(0, n):
    v = list(input())
    room.append(v)

if k == 0:
    for i in range(0, n):
        for j in range(0, m):
            if 'B' == room[i][j]:
                print(room[i][j])


