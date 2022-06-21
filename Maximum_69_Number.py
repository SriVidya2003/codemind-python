n=int(input())
arr=[]
k=0
while n!=0:
    r=n%10
    arr.append(r)
    k+=1
    n//=10
for i in range(k-1,-1,-1):
    if arr[i]==6:
        arr[i]=9
        break
for i in range(k-1,-1,-1):
    print(arr[i],end='')