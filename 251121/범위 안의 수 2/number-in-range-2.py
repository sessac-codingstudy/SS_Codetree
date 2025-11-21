answer = 0
count = 0
for _ in range(10):
    a = int(input())
    if 0<=a<=200:
        answer += a
        count += 1
print(answer, round(answer/count, 1))