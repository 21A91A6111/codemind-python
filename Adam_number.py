x = int(input())
n = x**2
s=0
while x!=0:
    v = x%10
    s = s*10+v
    x=x//10
m = s**2
a=0
while m!=0:
    c = m%10
    a = a*10+c
    m = m//10
if n==a:
    print("True")
else:
    print("False")