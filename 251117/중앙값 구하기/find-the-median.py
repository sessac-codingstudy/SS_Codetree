a,b,c = map(int,input().split())

if (a > b and a < c) or (a > c and a < b):
    mid = a
elif (b > a and b < c) or (b > c and b < a):
    mid = b
else:
    mid = c

print(mid)