a=int(input())
arr=list(map(int,input().split()))
for i in range(1,1000):
    if i in arr:
        continue
    else:
        print(i)
        break