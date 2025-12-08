nums = list(map(int, input().split()))
a=0
for n in nums:
    if n % 3 ==0:
        a=n
        break
i = nums.index(a)
print(nums[i-1])