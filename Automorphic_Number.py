n=int(input())
temp=n
c=0
while(n>0):
    n=n//10
    c=c+1
n=temp*temp
n=n%(pow(10,c))
if(temp==n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")