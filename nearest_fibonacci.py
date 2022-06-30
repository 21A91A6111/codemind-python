a=int(input())
arr=[]
fa=0
fb=1
fn=fa+fb
for i in range(100):
    arr.append(fa)
    fn=fa+fb
    fa=fb
    fb=fn
f=l=df=fl=0
for i in range(100):
    if arr[i]>a:
        l=arr[i]
        f=arr[i-1]
        dl=l-a
        df=a-f
        if df==dl:
            print(f,l)
        elif df>dl:
            print(l)
        elif df<dl:
            print(f)
        break