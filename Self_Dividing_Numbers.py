a=int(input())
b=int(input())
temp=0
count=0
r=0
m=0
for i in range(a,b+1):
    count=0
    temp=i
    while temp>0:
        r=temp%10
        if r==0 or i%r!=0:
            break
        temp=temp//10
    if temp==0:
        print(i,end=" ")
            