S = int(input())
# 1h = 3600秒
h = S//3600
m = (S - 3600*h)//60
s = S - 3600*h - 60*m
# print(h, m, s, sep=':') 下のような書き方がある
print(f'{h}:{m}:{s}')
