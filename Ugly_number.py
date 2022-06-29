num = int(input())
x=0
while num!=1:
    if num%2==0:
        num=num//2
    elif num%3==0:
        num=num//3
    elif num%5==0:
        num=num//5
    else:
        print('Not Ugly Number')
        x=x+1
        break
if(x==0):
    print('Ugly Number')