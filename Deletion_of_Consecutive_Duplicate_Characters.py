n=int(input())
for i in range(n):
    s=input()
    if (s.count(s[0])==len(s)):
        print(len(s)-1)
    else:
        c=0
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                c+=1
        print(c)
