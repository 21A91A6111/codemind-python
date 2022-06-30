t=int(input())
for k in range(t):
    a=input()
    dc=0
    for i in a:
        if i.isdigit():
            dc+=1
    if dc!=0:
        print("Yes")
    else:
        print("No")