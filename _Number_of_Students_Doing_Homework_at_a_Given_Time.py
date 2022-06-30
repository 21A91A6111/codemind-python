a=int(input())
arr=list(map(int,input().split()))
b=int(input())
brr=list(map(int,input().split()))
t=int(input())
c=0
for i in range(a):
    if t>=arr[i] and t<=brr[i]:
        c+=1
print(c)