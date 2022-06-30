a=int(input())
arr=list(map(int,input().split()))
b=int(input())
brr=list(map(int,input().split()))
f=0
for i in arr:
    if i in brr:
        f=1
    else:
        f=0
        break
if f==1:
    print("True")
else:
    print("False")