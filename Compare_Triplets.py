a=list(map(int,input().split()))
b=list(map(int,input().split()))
alice=bob=0
for i in range(3):
    if a[i]>b[i]:
        alice+=1
    if a[i]<b[i]:
        bob+=1
    if a[i]==b[i]:
        continue
print(alice,bob)