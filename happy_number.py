import math
def digitsSquareSum(Number):
    Sum = rem = 0
    while Number > 0:
        rem = Number % 10
        Sum = Sum + math.pow(rem, 2)
        Number = Number // 10
    return Sum


Number = int(input())
Temp = Number

while Temp != 1 and Temp != 4:
    Temp = digitsSquareSum(Temp)

if Temp == 1:
    print("True")
else:
    print("False")