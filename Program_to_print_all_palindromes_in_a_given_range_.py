n=int(input())
m=int(input())
r=0
sum=0
temp=0
for i in range(n,m+1):
    temp=i
    sum=0
    temp=i
    sum=0
    while temp!=0:
        r=temp%10
        sum=sum*10+r
        temp=temp//10
        if i==sum:
            print(i,end=" ")