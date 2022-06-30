a,b=map(int,input().split())
lcm=1
for i in range(10000):
    if lcm%a==0 and lcm%b==0:
        break
    else:
        lcm+=1
print(lcm)