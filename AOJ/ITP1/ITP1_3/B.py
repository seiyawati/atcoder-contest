# while文を使った方がいい
i = 1
while True:
    _input = int(input())
    if _input > 0:
        print(f'Case {i}: {_input}')
        i += 1
    elif _input == 0:
        break


# for i in range(1, 10000):
#     _input = int(input())
#     if _input > 0:
#         print(f'Case {i}: {_input}')
#     elif _input == 0:
#         break
