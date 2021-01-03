n = int(input())
# 三次元配列
count = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
for _ in range(n):
    b, f, r, v = map(int, input().split())
    count[b-1][f-1][r-1] += v
for index, bil in enumerate(count):
    if index == 3:
        for i in range(3):
            print(' ' + ' '.join(map(str, bil[i])))
    else:
        for i in range(3):
            print(' ' + ' '.join(map(str, bil[i])))
        print('#'*20)
