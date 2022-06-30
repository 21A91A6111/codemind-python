s=input()
t=input()
st=[]
tt=[]
for i in s:
    if i=='#':
        st.pop()
    else:
        st.append(i)
for i in t:
    if i=='#':
        tt.pop()
    else:
        tt.append(i)
if st==tt:
    print("True")
else:
    print("False")