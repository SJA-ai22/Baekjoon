a, A = map(int, input().split())
b, B = map(int, input().split())
c, C = map(int, input().split())
d, D = 0, 0
if a == b:
    d = c
    if A == C:
        D = B
    else:
        D = A
elif b == c:
    d = a
    if A == C:
        D = B
    else:
        D = C
else:
    d = b
    if B == C:
        D = A
    else:
        D = C
print(d, D)