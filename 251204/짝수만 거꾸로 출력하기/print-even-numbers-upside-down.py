n = int(input())

nums = list(map(int, input().split()))
answer = []
for i in range(n):
    if nums[i]%2==0:
        answer.append(nums[i])

for i in range(len(answer)-1,-1,-1):
    print(answer[i], end = ' ')
