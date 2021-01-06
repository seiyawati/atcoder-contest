while True:
    s = input()
    # breakを入れる位置にきおつける
    if s == '-':
        break
    m = int(input())
    for i in range(m):
        h = int(input())
        s = s[h:] + s[:h]
    print(s)