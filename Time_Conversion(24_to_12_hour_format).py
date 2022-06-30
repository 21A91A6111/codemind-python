a=input()
hour=(ord(a[0])-48)*10+ord(a[1])-48
minute=(ord(a[3])-48)*10+ord(a[4])-48
if hour==0:
    print("12",end="")
    print(":",end="")
    if minute>=10:
        print(minute,"AM")
    else:
        print("0",end="")
        print(minute,"AM")
elif hour==24:
    hour-=12
    print(hour,end="")
    print(":",end="")
    if minute>=10:
        print(minute,"AM")
    else:
        print("0",end="")
        print(minute,"AM")
elif hour==12:
    print(hour,end="")
    print(":",end="")
    if minute>=10:
        print(minute,"PM")
    else:
        print("0",end="")
        print(minute,"PM")
elif hour>12:
    hour-=12
    if hour<10:
        print("0",end="")
        print(hour,end="")
    else:
        print(hour,end="")
    print(":",end="")
    if minute>9:
        print(minute,"PM")
    else:
        print("0",end="")
        print(minute,"PM")
elif hour<12:
    if hour<10:
        print("0",end="")
        print(hour,end="")
    else:
        print(hour,end="")
    print(":",end="")
    if minute>=10:
        print(minute,"AM")
    else:
        print("0",end="")
        print(minute,"AM")