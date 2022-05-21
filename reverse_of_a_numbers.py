x= int(input())
a=0
while (x!=0):
    h= x%10
    a=a*10+h
    x= x//10
print(a)