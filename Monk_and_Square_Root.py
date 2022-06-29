t=int(input())
while t>0:
    a,b=map(int,input().split())
    min=-1
    for i in range(0,b):
        if(i*i)%b==a:
            min=i
            break
    print(min)    