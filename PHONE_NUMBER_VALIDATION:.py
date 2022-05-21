x=int(input())
c=0
while x!=0:
    b=x%10
    c+=1
    x=x//10
if(c==10):
    print("Valid")
else:
    print("Invalid")