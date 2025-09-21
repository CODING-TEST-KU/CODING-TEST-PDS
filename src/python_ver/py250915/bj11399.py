n=int(input())
nums=list(map(int,input().split()))

nums.sort()
result=0

for i in range(n):
    result+=(n-i)*nums[i]

print(result)
