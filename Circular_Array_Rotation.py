a,b,c=map(int,input().split())
arr=list(map(int,input().split()))
arr2=[]
for i in range(c):
    v=int(input())
    arr2.append(v)
for i in range(b):
    temp=arr[0]
    arr[0]=arr[a-1]
    for j in range(1,a):
        val=arr[j]
        arr[j]=temp
        temp=val
for i in arr2:
    print(arr[i])