a=int(input())
for i in range(a):
    for j in range(1,a-1):
        print(j,end="")
    for j in range(a-3,0,-1):
        print(j,end="")
    print()