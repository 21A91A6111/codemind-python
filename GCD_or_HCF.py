a, b = map(int, input().split())
while a!=b:
    if a>b:
        a=a-b
    elif a<b:
        b=b-a
print(a)