t=int(input())
s=input()
a="."
c=0
for i in range(len(s)):
    if s[i] in a:
        c+=1
if(c>t//2):
    print("YES") 
    for i in range(len(s)):
        if s[i] in a: 
            print("B",end="")
        else: 
            print(s[i],end="")
else: 
    print("NO")