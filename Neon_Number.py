n=int(input())
s=n*n
r=0
sum=0
while(s>0):
    r=s%10
    sum=sum+r
    s=s//10
if(sum==n):
    print("Neon Number")
else:
    print("Not Neon Number")