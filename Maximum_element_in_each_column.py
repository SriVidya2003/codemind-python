n,m=list(map(int,input().split()))
arr=[list(map(int,input().split()))
for i in range(n)]
for j in range(0,m):
    max=0
    for i in range(0,n):
        if arr[i][j]>max:
            max=arr[i][j]
    print(max)        