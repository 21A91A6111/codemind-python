def reverseNumber(number):
        x = 0
        n = abs(number)
        rev = 0
        while(n > 0):
            a = n % 10
            rev = rev * 10 + a
            n = n // 10
        if(number < 0):
            return ("-" + str(rev) )
        return (rev)
number = int(input())
print(reverseNumber(number))
