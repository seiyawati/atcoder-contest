# 基本的な全探索
S = input()
acgt = ['A', 'C', 'G', 'T']
# 今現在の連続している文字と、それまでで一番連続した文字の長さを比較する
m = 0
bm = 0
for s in S:
    if s in acgt:
        m += 1
    else:
        bm = max(m, bm)
        m = 0
print(max(m, bm))
