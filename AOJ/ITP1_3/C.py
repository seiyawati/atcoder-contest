while True:
    _arr = list(map(int, input().split()))
    _arr.sort()
    if _arr[0] == 0 and _arr[1] == 0:
        break
    else:
        print(f'{_arr[0]} {_arr[1]}')