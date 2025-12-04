nums = list(map(int, input().split()))

answer = []
for i in range(10):
    if nums[i] == 0:
        break
    if nums[i] % 2 ==0:
        answer.append(nums[i])

print(len(answer), sum(answer))

