n = int(input())

answer = 0
count = 0
for _ in range(n):
    a = int(input())
    answer += a
    count += 1
print(answer, round(answer/count,1))