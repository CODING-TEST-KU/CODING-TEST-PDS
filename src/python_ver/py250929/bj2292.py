
# 1 7 19 37 61
# 6 12 18 24
# 1  2  3  4
# 1  3  6  10

n = int(input())

# 해당 둘레까지 이동
layer = 1
end = 1
add = 6

while end < n:
    end += add
    layer += 1
    add += 6

print(layer)
