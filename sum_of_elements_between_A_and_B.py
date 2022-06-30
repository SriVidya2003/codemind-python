n=int(input())
arr=list(map(int,input().split()))
sum=0
a,b=map(int,input().split())
for i in range(len(arr)):
    if arr[i]>=a and arr[i]<=b:
        sum+=arr[i]
print(sum)