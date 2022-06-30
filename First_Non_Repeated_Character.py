t=int(input())
for i in range(t):
    n=int(input())
    w=""
    s=input()
    q=0
    for i in range(n):
        if s[i] not in w and s.count(s[i])==1:
            w+=s[i]
            q=1
            break
    if(q==0):
        print(-1)
    else:
        print(w)
