n = int(input())
S = []
H = []
C = []
D = []
rank_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
label = ''
for _ in range(n):
    gara, rank = map(str, input().split())
    if gara == 'S':
        S.append(int(rank))
    elif gara == 'H':
        H.append(int(rank))
    elif gara == 'C':
        C.append(int(rank))
    else:
        D.append(int(rank))
def judge(arr):
    if arr == S:
        label == 'S'
    elif arr == H:
        label == 'H'
    elif arr == C:
        label == 'C'
    else:
        label == 'D'
    arr.sort()
    # 差集合をとることができる
    rank_diff = set(rank_list) ^ set(arr)
    for i in list(rank_diff):
        print(label+' '+str(i))
label = 'S'
judge(S)
label = 'H'
judge(H)
label = 'C'
judge(C)
label = 'D'
judge(D)

    
