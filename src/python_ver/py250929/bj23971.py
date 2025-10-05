h,w,n,m=map(int, input().split())

rows=(h+n)//(n+1)
cols=(w+m)//(m+1)

print(rows*cols)