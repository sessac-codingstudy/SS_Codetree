count = 0
while count < 4:
    n = int(input())
    count += 1
    if n % 2 ==1:
        continue
    else:
        print(n//2)