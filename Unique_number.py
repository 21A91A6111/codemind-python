n=int(input())
lst=[]
r=0
while n!=0:
    r=n%10
    lst.append(r)
    n=n//10
if len(set(lst))==len(lst):
    print("Unique Number")
else:
    print("Not Unique Number")