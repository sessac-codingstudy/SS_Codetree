start, end = map(int, input().split())

answer = []
count = 0
# Please write your code here.
for i in range(start, end+1):
    for j in range(1, i+1):
        if i % j == 0:
            answer.append(j)
    if len(answer) == 3:
        count += 1
    answer.clear()

print(count)