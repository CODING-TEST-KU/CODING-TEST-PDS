N = int(input())
A = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

A.sort()

for num in nums:
    exists=False
    start,end=0,len(A)-1

    while start<=end:
        mid=int((start+end)/2)
        if A[mid]==num:
            exists=True
            break
        elif A[mid]<num:
            start=mid+1
        else:
            end=mid-1

    if exists:
        print(1)
    else:
        print(0)

