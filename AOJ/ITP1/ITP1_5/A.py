while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    else:
        for _ in range(H):
            for _ in range(W):
                length += '#'
            print(length)
        print('')

# for i in range(8):
#     end=''とすることで改行されないで出力される
#     print("#", end="")
# print()