string = input()
c=0
d=0
str=0;
while str < len(string):
    if(string[str] == 'z'):
        c+=1
    elif(string[str] =='o'):
        d+=1
    str+=1
if(2*c == d):
    print("Yes")
else:
    print("No")