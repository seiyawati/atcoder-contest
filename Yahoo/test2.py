import copy
N, K = map(int, input().split())
book = []
for i in range(N):
    lin = input().split()
    if len(lin) > 1:
        n = lin[1]
        book.append(int(n))
        print(n)
    else:
        new_book = book.copy()
        del new_book[-K:]
        print(max(new_book))
