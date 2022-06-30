def ispangram(str):
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for ch in alphabet:
        if ch not in str.upper():
            return False
    return True
str=input()
if ispangram(str)==True:
    print("True")
else:
    print("False")