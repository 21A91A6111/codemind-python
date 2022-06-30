a=int(input())
arr=list(map(int,input().split()))
arr.sort()
dis=[]
for i in arr:
    if i not in dis:
        dis.append(i)
if len(dis)<3:
    print(max(dis))
else:
    print(dis[len(dis)-3])