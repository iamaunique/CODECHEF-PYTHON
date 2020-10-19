# cook your dish here
for _ in range(int(input())):
    N,MINX,MAXX = map(int,input().split())
    num = MAXX-MINX+1
    even = num//2
    odd = num-even
    for i in range(N):
        w, b = map(int,input().split())
        if w%2==0 and b%2==0:
            even = even+odd
            odd=0
        elif w%2==1 and b%2==1:
            even,odd = odd,even
        elif w%2==0 and b%2==1:
            odd= even+odd
            even=0
    print(even,odd)
