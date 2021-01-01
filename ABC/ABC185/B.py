N, M, T = map(int, input().split())
bat = N
last_B = 0
for _ in range(M):
    A, B = map(int, input().split())
    bat -= A-last_B
    if bat <= 0:
        print('No')
        break
    else:
        bat += (B-A)
        if bat > N:
            bat = N
        last_B = B
else:
    bat -= T-last_B
    if bat <= 0:
        print('No')
    else:
        print('Yes')
    