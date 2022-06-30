arr=list(map(str,input().split()))
a=int(input())
ff=0
for i in range(a):
    brr=list(map(str,input().split()))
    f=0
    for j in brr:
        if j in arr:
            f=1
        else:
            f=0
            break
    if f==1:
        ff=1
    else:
        ff=0
        break
if ff==1:
    print("True")
else:
    print("False")