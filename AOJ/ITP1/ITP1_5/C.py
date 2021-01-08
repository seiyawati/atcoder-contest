while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    else:
        for i in range(1, H+1):
            if i%2 == 1:
                for j in range(1, W+1):
                    if j%2 == 1:
                        print('#', end='')
                    else:
                        print('.', end='')
            else:
                for k in range(1, W+1):
                    if k%2 == 1:
                        print('.', end='')
                    else:
                        print('#', end='')
            print('', end='\n')
    print('')


# 別解
# (i+j)%2 == 1 or (i+j)%2 == 0 時で場合わけする
# こっちの方がシンプルにかける