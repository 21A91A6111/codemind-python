n = int(input())
n = str(n)
n = list(n)
n.reverse()
c=0
for i in range(len(n)):
    k = int(n[i])
    c+=k*8**i
b=bin(c)
b = b[2:]
print(b)