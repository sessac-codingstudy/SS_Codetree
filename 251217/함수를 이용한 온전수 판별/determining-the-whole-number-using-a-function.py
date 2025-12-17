a, b = map(int, input().split())

# Please write your code here.
def sol(a,b):
    count = 0
    for i in range(a,b+1):
        if i % 2 ==0:
            continue
        elif i%10 == 5:
            continue
        elif i%3==0 and i%9!=0:
            continue
        else:
            count+=1
    return count

print(sol(a,b))
