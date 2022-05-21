def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
a=n
res=0
while n!=0:
    temp=n%10
    res=res*10+temp;
    n//=10
if prime(a) and prime(res):
        print('circular prime')
elif prime(a):
    print('prime but not a circular prime')
else:
    print('not prime')