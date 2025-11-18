A,B = map(int, input().split())

a = A//B
b = A%B

answer = []
for _ in range(20):
    b *= 10
    answer.append(str(b//B))
    b %= B

print(f"{a}.{''.join(answer)}")
