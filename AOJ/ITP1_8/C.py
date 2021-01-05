import string
import sys
alpha = list(string.ascii_lowercase)
sum = [0 for x in range(26)]
# 複数行の入力を一つの文字列に
S = sys.stdin.read().lower()
for s in S:
    for i in range(26):
        if s == alpha[i]:
            sum[i] += 1

for i in range(26):
    print(f"{alpha[i]} : {sum[i]}")    

# 複数行の入力をリストにする
# s = sys.stdin.readlines()
