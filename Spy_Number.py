n=int(input())
prod=1
sum=0
r=0
while n>0:
    r=n%10
    sum=sum+r
    prod=prod*r
    n=n//10
if sum==prod:
    print("Spy Number")
else:
    print("Not Spy Number")