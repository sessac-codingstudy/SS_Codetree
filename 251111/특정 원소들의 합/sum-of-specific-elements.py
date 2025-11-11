count = 0
for i in range(1,5):
    answer = list(map(int, input().split()))
    for j in range(i):
        count += answer[j]
print(count)