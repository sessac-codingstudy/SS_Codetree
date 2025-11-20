n = int(input())
day12 = 0
day3 = 0
day2 = 0
for i in range(1, n+1):
    if i % 12 == 0:
        day12 += 1
    elif i % 3 ==0:
        day3 += 1
    elif i % 2 == 0:
        day2 += 1
    
print(day2, day3, day12)