a, b = map(int, input().split())
S = a*b
L = 2*(a+b)
# print関数はカンマで区切るとスペースが入る, sep=''オプションで繋ぎ文字を決めれる
print(S, L)