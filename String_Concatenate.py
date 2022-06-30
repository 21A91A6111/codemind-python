def sort(s):
    s1=""
    arr=[]
    for i in s:
        arr.append(i)
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    for i in arr:
        s1+=i
    return s1
a=input()
b=input()
res=a+b
print(sort(res))