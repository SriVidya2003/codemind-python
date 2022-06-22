n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==n-1 or j==n:
            continue
        else:
            print(j,end="")
    for j in range(1,n-2):
        print(j,end="")
    print()    