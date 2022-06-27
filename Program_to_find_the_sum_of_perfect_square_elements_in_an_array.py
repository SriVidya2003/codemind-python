n=int(input())
arr=list(map(int,input().split()))
sum=0
for i in range(len(arr)):
    count=0
    k=arr[i]
    for j in range(1,k+1):
        if arr[i]==j*j:
            count=1
            break
    if count==1:
        sum=sum+arr[i]
print(sum)    