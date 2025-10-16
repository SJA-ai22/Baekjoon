n = int(input())
arr = list(map(int, input().split()))

max = -1000
stp = 0

for i in arr:
    stp += i
    if max < stp:
        max = stp
    if stp <= 0:
        stp = 0

print(max)