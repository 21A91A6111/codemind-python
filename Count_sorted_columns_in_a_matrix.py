def col_sor(l):
    m=sorted(l)
    n=sorted(l,reverse=True)
    return l==m or l==n
a,b=map(int,input().split())
mat=[]
for i in range(a):
    x=list(map(int,input().split()))
    mat.append(x)
cnt=0
for i in range(b):
    z=[]
    for j in range(a):
        z.append(mat[j][i])
    if col_sor(z):
        cnt+=1
print(cnt)