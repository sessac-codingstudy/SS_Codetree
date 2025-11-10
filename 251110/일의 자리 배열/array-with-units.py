a, b = map(int, input().split())

answer = [a,b]
print(a, b, end = ' ')
for i in range(8):
    result = (answer[i]+answer[i+1])%10
    answer.append(result)
    print(result, end = ' ')

