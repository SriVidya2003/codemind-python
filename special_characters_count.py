n=input()
count=0
for char in n:
    if char.isalpha():
        continue
    elif char.isdigit():
        continue
    elif char==" ":
        continue
    else:
        count=count+1
print(count)