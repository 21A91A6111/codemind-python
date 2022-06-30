a=input()
vo=['a','e','i','o','u','A','E','I','O','U']
vow=con=dig=spa=0
for i in a:
    if i.isdigit():
        dig+=1
    elif i==" ":
        spa+=1
    else:
        if i in vo:
            vow+=1
        else:
            con+=1
print("Vowels:",vow)
print("Consonants:",con)
print("Digits:",dig)
print("White spaces:",spa)