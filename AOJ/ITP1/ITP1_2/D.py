W, H, x, y, r = map(int, input().split())
# 座標の負の方向にはみ出す時を考える
if x+r<=W and y+r<=H and x-r>=0 and y-r>=0:
    print('Yes')
else:
    print('No')