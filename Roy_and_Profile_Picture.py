l=int(input())
n=int(input())
for i in range(0,n):
    w,h=map(int,input().split())
    if w<l or h<l:
        print("UPLOAD ANOTHER")
    elif w==h:
        print("ACCEPTED")
    elif w==l and h==l:
        print("ACCEPTED")
    elif w>l or h>l:
        print("CROP IT")