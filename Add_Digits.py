def addDigits(num):
    
    while(num>=10):
        temp=0
        while(num>0):
            temp=temp+num%10
            num=num//10
            
        num=temp
        
    return num
num=int(input())
print(addDigits(num))