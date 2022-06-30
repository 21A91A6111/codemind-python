a,b=map(int,input().split())
hcf=1
for i in range(1,max(a,b)):
    if a%i==0 and b%i==0:
        hcf=i
print(hcf)