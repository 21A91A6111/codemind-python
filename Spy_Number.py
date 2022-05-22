n=int(input())
sum,pro=0,1
while n>0:
    d=n%10
    sum+=d
    pro*=d
    n//=10
if(sum==pro):
    print('Spy Number')
else:
    print('Not Spy Number')