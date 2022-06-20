s=input()
p=input()
count=0
for ch in s:
    if ch==p:
        count+=1
if count>0:
    print(count)
else:
    print(-1)