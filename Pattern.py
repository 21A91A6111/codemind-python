a=int(input())
for i in range(a):
    for j in range(a-(i+1)):
        print(" ",end="")
    for j in range(i+1):
        print(j+1,end="")
    for j in range(i-1,-1,-1):
        print(j+1,end="")
    print(""),