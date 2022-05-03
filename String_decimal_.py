t=int(input())
count=0
while t>0:
    s=input()
    count=0
    if s.isdecimal():
        print("True")
    else:
        print("False")
    t=t-1