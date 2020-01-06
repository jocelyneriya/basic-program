int_num = list(map(int,input().split()))
A,B,C = sorted(int_num)
if A**2+B**2==C**2:
    print("yes")
else:
    print("no")
