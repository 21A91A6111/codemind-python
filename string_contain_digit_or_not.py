a=input()
dc=0
for i in a:
    if i.isdigit():
        dc+=1
if dc>0:
    print("Contains",dc,"digit")
else:
    print("Doesn't contain digit")