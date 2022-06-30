s1=input()
s2=input()
x=s1.lower()
y=s2.lower()
if len(x)==len(y):
    a=sorted(x)
    b=sorted(y)
    if a==b:
        print("True")
    else:
        print(False)
else:
    print("False")