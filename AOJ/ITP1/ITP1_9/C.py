n = int(input())
men = 0
women = 0
for i in range(n):
    m, w = map(str, input().split())
    # 文字列の大きい小さいは辞書順できまる
    if m > w:
        men += 3
    elif m < w:
        women += 3
    else:
        men += 1
        women += 1
print(f"{men} {women}")
