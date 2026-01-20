n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
answer = []
for s in str:
    if s.startswith(t):
        answer.append(s)


print(sorted(answer)[k-1])