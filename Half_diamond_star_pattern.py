a=int(input())
if a>=3 and a<=100:
    for i in range(1,a+1):
        for j in range(1,i+1):
            print("*",end="")
        print(""),
    for i in range(a-1,0,-1):
        for j in range(1,i+1):
            print("*",end="")
        print(""),
else:
    print("The pattern is not possible")