# 問題文をよく読む必要がある、出力結果が小数点切り捨てだから//
while True:
    a, op, b = map(str, input().split())
    if op == "+":
        print(int(a) + int(b))
    elif op == "-":
        print(int(a) - int(b))
    elif op == "*":
        print(int(a)*int(b))
    elif op == "/":
        print(int(a)//int(b))
    else:
        break