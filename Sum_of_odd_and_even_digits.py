n=int(input())
arr=list(map(int,input().split()))
even=0
odd=0
diff=0
for i in range(len(arr)):
    if i%2==0:
        even=even+arr[i]
    else:
        odd=odd+arr[i]
diff=odd-even
if diff==0:
    print("YES")
else:
    print("NO")