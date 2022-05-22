a=int(input())
c=a*a
s=0
while c!=0:
    i=c%10
    s+=i
    c=c//10
sum=int(s)
if(a==sum):
    print('Neon Number')
else:
    print('Not Neon Number')