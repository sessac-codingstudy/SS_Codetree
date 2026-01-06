M, D = map(int, input().split())

# Please write your code here.

def sol(M,D):
    if M in [1,3,5,7,8,10,12]:
        if D <32:
            print("Yes")
        else:
            print("No")
    elif M in [4,6,9,11]:
        if D <31:
            print("Yes")
        else:
            print("No")
    elif M == 2:
        if D <29:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

sol(M,D)

            
