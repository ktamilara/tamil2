n1=int(input())
l1=list(map(int,input().split()))

c1=0
for i in range(0,n1+1):
    if n1*i in l1:
        c1=c1+1
print(c1)      
