n=input()
w=""
for i in range(len(n)):
    for j in range(i,len(n)):
        if n[j] not in w and n[j].upper() not in w and n[j].lower() not in w:
            w+=n[j]
        else:
            break
    if(len(w)<3):
        w=""
        continue
    else:
        break
if len(w)<3:
    print(-1)
else:
    print(w)