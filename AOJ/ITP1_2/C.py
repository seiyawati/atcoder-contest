# a, b, c = map(int, input().split())
# _arr = [a, b, c]
# _min = min(_arr)
# _arr.remove(_min)
# _max = max(_arr)
# _arr.remove(_max)
# print(_min, _arr[0], _max)

_list = list(map(int, input().split()))
# 小さい順にソート
_list.sort()
print(_list[0], _list[1], _list[2])