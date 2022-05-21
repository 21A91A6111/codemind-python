def check_palindrome(v):
    if len(v) < 1:
        return True
    else:
        if v[0] == v[-1]:
            return check_palindrome(v[1:-1])
        else:
            return False

var = input()
if(check_palindrome(var)):
    print("True")
else:
    print("False")