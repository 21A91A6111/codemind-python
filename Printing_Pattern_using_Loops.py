a=int(input())
k=a
for i in range(1,2*a):
    k=a
    if i<=a:
        for j in range(1,2*a):
            print(k,end=" ")
            if i>j:
                k-=1
            if i+j>=2*a:
                k+=1
    if i>a:
        for j in range(1,2*a):
            print(k,end=" ")
            if i+j<2*a:
                k-=1
            if j>=i:
                k+=1
    print()