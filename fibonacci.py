a=int(input())
fa=0
fb=1
n=0
for i in range(a):
    print(fa,end=" ")
    n=fa+fb
    fa=fb
    fb=n