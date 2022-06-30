n=int(input())
arr=list(map(int,input().split()))
count=0
for i in range(n-2):
    if(arr[i]%2!=0 and arr[i+2]%2==0) or (arr[i]%2==0 and arr[i+2]%2!=0):
        count+=1
print(count)