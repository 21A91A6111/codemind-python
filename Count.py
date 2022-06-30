a=int(input())
arr=list(map(int,input().split()))
se=so=0
for i in arr:
    if i%2==0:
        se+=1
    else:
        so+=1
print(se,so)