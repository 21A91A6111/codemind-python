#include<stdio.h>
t=int(input())
for i in range(t):
    
    n=int(input())
    arr=list(map(int,input().split()))
    c=0
    for i in range(n):
        if(arr[i]%2==1):
            c+=1
    if(c%2==1):
        c-=1
    print(c//2)
