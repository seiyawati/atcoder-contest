N = int(input())
count = 0
# rangeの第三引数にstepを指定
# 約数の個数を求めるプログラム
for i in range(1, N+1, 2):
    yaku = 0
    for j in range(1, N+1):
        if i%j == 0:
            yaku += 1
    if yaku == 8:
        count += 1
print(count)
