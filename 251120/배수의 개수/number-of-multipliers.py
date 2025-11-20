answer3 = 0
answer5 = 0
for _ in range(10):
    a = int(input())
    if a % 3 == 0:
        answer3 += 1
    if a % 5 == 0:
        answer5 += 1
print(answer3, answer5)