count = 0
while count < 3:
    n = int(input())
    if n % 2 == 0:      # 짝수일 때만 처리
        print(n // 2)
        count += 1      # 짝수 처리 개수 증가

        