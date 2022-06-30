a=input()
hour=(ord(a[0])-48)*10+ord(a[1])-48
minute=(ord(a[3])-48)*10+ord(a[4])-48
ampm=a[6]
am="AM"
pm="PM"
if hour==12 and ampm in am:
    print("00:",end="")
    if minute<10:
        print("0",end="")
        print(minute)
    else:
        print(minute)
elif hour==12 and ampm in pm:
    print("12:",end="")
    if minute<10:
        print("0",end="")
        print(minute)
    else:
        print(minute)
elif ampm in am:
    if hour<10:
        print("0",end="")
        print(hour,end="")
    else:
        print(hour,end="")
    print(":",end="")
    if minute<10:
        print("0",end="")
        print(minute)
    else:
        print(minute)
elif ampm in pm:
    hour+=12
    if hour<10:
        print("0",end="")
        print(hour,end="")
    else:
        print(hour,end="")
    print(":",end="")
    if minute<10:
        print("0",end="")
        print(minute)
    else:
        print(minute)