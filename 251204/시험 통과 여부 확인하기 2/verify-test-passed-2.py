n = int(input())

count = 0
for _ in range(n):
    a,b,c,d = map(int, input().split())
    if (a+b+c+d)/4 >= 60:
        print("pass")
        count += 1
    else:
        print("fail")

print(count)