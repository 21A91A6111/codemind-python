n=int(input())
res=0
for i in range(n):
    v=input()
    x=list(v.split())
    for j in x:
        if j=="++X":
            res+=1
        elif j=="X++":
            res+=1
        elif j=="--X":
            res-=1
        elif j=="X--":
            res-=1
print(res)

