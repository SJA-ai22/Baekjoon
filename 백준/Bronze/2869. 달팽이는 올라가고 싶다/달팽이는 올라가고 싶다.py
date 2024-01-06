import math
a,b, v = map(int, input().split())
day = 1 + math.ceil((v-a)/(a-b))
print(day)