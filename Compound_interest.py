x,y,z = map(int,input().split())
p = x*((1+y/100)**z)
print("%.2f"%p)