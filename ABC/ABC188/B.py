N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
goukei = 0
for i in range(N):
    goukei += A[i]*B[i]
if goukei == 0:
    print('Yes')
else:
    print('No')