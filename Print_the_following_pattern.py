a=int(input())
arr=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for i in range(a):
    for j in range(a-(i+1)):
        print(" ",end="")
    for j in range(i+1):
        print(arr[j],end="")
    for j in range(i-1,-1,-1):
        print(arr[j],end="")
    print(""),