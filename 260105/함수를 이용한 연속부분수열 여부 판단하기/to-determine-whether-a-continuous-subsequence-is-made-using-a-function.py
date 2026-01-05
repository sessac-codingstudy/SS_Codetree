n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def sol(a,b):
    answer = "No"
    for i in range(len(a)-len(b)+1):
        if a[i:i+n2] == b:
            answer = "Yes"
    return answer

print(sol(a,b))

    
        