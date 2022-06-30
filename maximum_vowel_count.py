s=input()
n=s.split()
max=0
m=0
for word in n:
    count=0
    for char in word:
        if char=='a' or char=='e' or char=='i' or char=='o' or char=='u'or char=='A' or char=='E' or char=='I' or char=='O' or char=='U':
            count=count+1
        if count>max:
            max=count
print(max)
    