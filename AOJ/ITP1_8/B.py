while True:
    v = input()
    sum = 0
    if v == '0':
        break
    else:
        for i in v:
            sum += int(i)
        print(sum)
