N = int(input())

for score in range(N, 101):
    if score >= 90:
        print("A", end = ' ')
    elif 80 <= score < 90:
        print("B", end = ' ')
    elif 70 <= score < 80:
        print("C", end = ' ')
    elif 60 <= score < 70:
        print("D", end = ' ')
    else:
        print("F", end = ' ')