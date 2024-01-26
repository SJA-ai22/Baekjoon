n = int(input())
count = 0
data = 666
while True:
    if '666' in str(data):
        count += 1
    if n == count:
        break
    data += 1
print(data)