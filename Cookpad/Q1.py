import sys

dish1 = sys.argv[1]
dish2 = sys.argv[2]

word = ''

flag = -1
while True:
    if dish1[flag] == dish2[flag]:
        word += dish1[flag]
        flag -= 1
    else:
        break

word = ''.join(list(reversed(word)))
print(word)

    