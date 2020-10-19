# cook your dish here
for _ in range(int(input())):
    n=int(input())
    L=list(map(int,input().split()))
    s=set(L)
    
    if(0 in s ):
        print(len(s)-1)
    else:
        print(len(s))
