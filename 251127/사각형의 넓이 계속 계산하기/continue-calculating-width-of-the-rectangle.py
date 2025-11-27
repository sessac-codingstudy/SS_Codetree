while True:
    a,b,c = map(str, input().split(' '))
    a,b = int(a), int(b)
    print(a*b)
    if c == 'C':
        break
