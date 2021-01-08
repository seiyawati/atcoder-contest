# 全探索の基本中の基本
N = int(input())
for i in range(1, 10):
    for j in range(1, 10):
        if i*j == N:
            print('Yes')
            # インタラクティブなs処理の終了はbreakではなくてexit
            exit()
print('No')
