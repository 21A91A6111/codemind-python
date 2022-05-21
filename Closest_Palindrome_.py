def palin(n):
    m=n
    s=0
    while m!=0:
        v = m%10
        s = s*10+v
        m = m//10
    if n==s:
        return n
x = int(input())
for i in range(x-1,1,-1):
    if palin(i):
        a=i
        break
y = x+1
while y!=0:
    if palin(y):
        b=y
        break
    y+=1
if (x-a)<(b-x):
    print(a)
elif (x-a)==(b-x):
    print(a,b)
else:
    print(b)