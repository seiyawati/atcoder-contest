while True:
    m, f, r = map(int, input().split())
    sum = m+f
    if  m==-1 and f==-1 and r==-1:
        break
    elif sum<30 or m==-1 or f==-1:
        print('F')
    elif sum>=80:
        print('A')
    elif sum>=65 and sum<80:
        print('B')
    elif sum>=50 and sum<65:
        print('C')
    elif sum>=30 and sum<50:
        if r>=50:
            print('C')
        else:
            print('D')