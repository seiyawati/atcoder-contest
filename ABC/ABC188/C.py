# PyPy3なら通る
import copy
N = int(input())
rate = list(map(int, input().split()))
rate_copy = copy.copy(rate)
for j in range(N-1):
    loose = []
    for i in range(len(rate)//2):
        loose.append(min(rate[2*i], rate[2*i+1]))
    for v in loose:
        rate.remove(v)
print(rate_copy.index(min(rate)) + 1)

# ブロックを二つにして考える
N = int(input())
a = list(map(int, input().split()))
half = len(a)//2
v = min(max(a[:half]), max(a[half:]))
print(a.index(v)+1)
