W = input()
count = 0
while True:
    Ti = input()
    if Ti == 'END_OF_TEXT':
        break
    else:
        for v in Ti.split(' '):
            if v.lower() == W:
                count += 1
print(count)

