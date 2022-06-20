n=int(input())
arr=list(map(int,input().split()))
r=0
k=0
count=0
k=0
m=0
for i in range(len(arr)):
    count=0
    k=arr[i]
    while k!=0:
        r=k%10
        count+=1
        k=k//10
    if count%2==0:
        m+=1
print(m)