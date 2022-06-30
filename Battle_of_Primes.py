def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return True
    else:
        return False
n1=int(input())
n2=int(input())
x=n1+n2
for i in range(x+1,100000):
    if prime(i):
        y=i
        break
print(y-x)