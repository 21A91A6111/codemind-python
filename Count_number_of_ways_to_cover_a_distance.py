def step(a):
    if(a<=0):
        return 0
    if(a==1):
        return 1
    if(a==2):
        return 2
    if(a==3):
        return 4
    return step(a-1)+step(a-2)+step(a-3)
n=int(input())
v=step(n)
print(v)
