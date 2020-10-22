# cook your dish here
try:
    t = int(input())
    for _ in range(t):
        r, c, k = map(int, input().rstrip().split(' '))
        if r <= k:
            start_row = 1
        else:
            start_row = r-k
        if c <= k:
            start_col = 1
        else:
            start_col = c-k
        if r+k >= 8:
            end_row = 8
        else:
            end_row = r+k
        if c+k >= 8:
            end_col = 8
        else:
            end_col = c+k

        print((end_row - start_row + 1)*(end_col - start_col + 1))
        
except:
    pass
