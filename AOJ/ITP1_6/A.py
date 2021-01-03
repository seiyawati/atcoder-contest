n = int(input())
arr = list(map(str, input().split()))
arr.reverse()
# 配列の要素を任意の区切り文字で結合
print(' '.join(arr))
