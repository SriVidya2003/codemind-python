s=input()
x=s.lower()
y='aeiou'
z=0
i=[]
for ch in x:
    if ch in y and ch in x:
        i.append(ch)
for ch in y:
    if ch not in i:
        z=1
        print(ch,end=" ")
if z==0:
    print("0")