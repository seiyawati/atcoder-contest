string = input()
q = int(input())
for i in range(q):
    _in = input().split()
    a = int(_in[1])
    b = int(_in[2])
    if _in[0] == 'replace':
        p = _in[3]
        string = string[:a] + p + string[b+1:]
    elif _in[0] == 'print':
        print(string[a:b+1])
    else:
        _re = string[a:b+1]
        # [::-1]で逆順に並べ替え
        string = string[:a] + _re[::-1] + string[b+1:]
