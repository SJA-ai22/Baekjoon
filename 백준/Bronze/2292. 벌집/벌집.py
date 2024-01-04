n = int(input())
room = 1
num = 1
while n > room:
    room += 6 * num
    num += 1
print(num)