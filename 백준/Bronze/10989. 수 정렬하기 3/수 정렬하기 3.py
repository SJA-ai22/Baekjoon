import sys

data = [0] * (10000 + 1)
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    data[int(input())] += 1
  
for i in range(len(data)):
    if data[i] != 0:
        for _ in range(data[i]):
            print(i)