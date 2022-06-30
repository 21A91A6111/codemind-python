def rev(a):
    s=0
    while a>0:
        rem=a%10
        s=(s*10)+rem
        a//=10
    return s
a=int(input())
arev=rev(a)
su=0
j=1
while arev>0:
    rem=arev%10
    su+=rem**j
    j+=1
    arev//=10
if su==a:
    print("True")
else:
    print("False")