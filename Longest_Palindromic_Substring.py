def rev(n):
    q=n[::-1]
    return q
s=input()
x=""
for i in range(len(s)):
    z=""
    for j in range(i,len(s)):
        z+=s[j]
        if z==rev(z):
            if len(x)<len(z):
                x=z
print(x)