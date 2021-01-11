A, B, K = map(int, input().split())
L = min(A, B)
arr = []
for i in range(1, L+1):
    if A%i==0 and B%i==0:
        arr.append(i)
# 破壊的処理, 大きい順に並べ替える
arr.reverse()
print(arr[K-1])    
