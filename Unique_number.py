n=int(input())
list=[]
r=0
while n!=0:
    r=n%10
    list.append(r)
    n=n//10
if len(set(list))==len(list):
    print("Unique Number")
else:
    print("Not Unique Number")