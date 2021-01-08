N = int(input())
S = input()
# print(S.count('ABC'))
count = 0
# 全桃李調べ上げる
for i in range(N-2):
    if S[i] == 'A' and S[i+1] == 'B' and S[i+2] == 'C':
        count += 1
    else:
        continue
print(count)
