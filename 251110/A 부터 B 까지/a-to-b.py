A, B = map(int, input().split())

answer = A
while True:
    print(answer, end = ' ')
    if answer % 2 == 1:
        answer *= 2
    elif answer % 1 == 0:
        answer += 3


    if answer > B:
        break
