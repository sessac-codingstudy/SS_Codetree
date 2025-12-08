nums = list(map(int, input().split()))

a ,b = 0, 0
# 홀수 합
for i in range(0,10,2):
    a += nums[i]
# 짝수 합
for j in range(1,10,2):
    b += nums[j]

print(max(a,b) - min(a,b))