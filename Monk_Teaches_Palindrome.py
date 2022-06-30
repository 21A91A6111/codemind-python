t=int(input())
for i in range(t):
    a=input()
    l=len(a)
    f=0
    for j in range(l):
        if a[j]==a[l-j-1]:
            f=1
        else:
            f=0
            break
    if f==1:
        if len(a)%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")