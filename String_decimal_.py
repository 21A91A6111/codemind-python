n=int(input())
for i in range(n):
    s=input()
    f=0
    for i in s:
        if i.isdigit():
            f=1
        else:
            f=0
            break
    if f==1:
        print(True)
    else:
        print(False)