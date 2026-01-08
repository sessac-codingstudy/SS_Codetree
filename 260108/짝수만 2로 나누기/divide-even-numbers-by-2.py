n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def sol(arr):
    for i in range(n):
        if arr[i]%2 == 0:
            arr[i] = arr[i] // 2
            print(arr[i], end = ' ')
        else:
            print(arr[i], end = ' ')
sol(arr)