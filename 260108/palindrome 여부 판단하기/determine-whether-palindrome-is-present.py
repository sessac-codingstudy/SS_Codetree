A = input()

# Please write your code here.
def sol(a):
    if a == a[::-1]:
        print("Yes")
    else:
        print("No")

sol(A)