import itertools
while True:
    count = 0
    n, x = map(int, input().split())
    if n==0 and x==0:
        break
    else:
        l = list(range(1, n+1))
        # 重複なしの組み合わせ
        b = itertools.combinations(l, 3)
        for v in b:
            if sum(v)==x:
                count += 1
    print(count)


# 上のプログラムを純粋なアルゴリズムを三重ループで求めた
# while True:
#     count = 0
#     n, x = map(int, input().split())
#     if n==0 and x==0:
#         break
#     else:
#         for i in range(1, n+1):
#             for j in range(i+1, n+1):
#                 for k in range(j+1, n+1):
#                     if i+j+k==x:
#                         count += 1
#     print(count)