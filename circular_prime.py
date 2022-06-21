n=int(input())
count=0
sum=0
for i in range(2,n):
    if n%i==0:
        count+=1
if count!=0:
    print("not prime")
else:
    c=0
    while(n!=0):
        r=n%10
        sum=sum*10+r
        n=n//10
    for i in range(2,sum):
        if sum%i==0:
            c+=1
    if c==0:
        print("circular prime")
    else:
        print("prime but not a circular prime")