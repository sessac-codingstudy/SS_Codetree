n = int(input())
nums = list(map(float, input().split()))

m = sum(nums)/n
print(f"{m:.1f}")
if m >= 4.0:
    print("Perfect")
elif 3.0 <= m < 4.0:
    print("Good")
else:
    print("Poor")