a = [0,1]
for i in range(4800):
    a.append(a[-1] + a[-2])
for i in range(int(input())):
    n = int(input())
    if n in a:
        print("YES")
    else:
        print("NO")
