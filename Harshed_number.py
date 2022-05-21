num =int(input())
sum =0
r =0
temp=num
while temp>0:
    r=temp%10
    sum = sum+r
    temp = temp//10
if(num%sum == 0):
    print("True")
else:
    print("False")