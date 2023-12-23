num = int(input())
for i in range(num):
    n, sen = input().split()
    result = ''
    for j in range(len(sen)):
        result += int(n)*sen[j]
    print(result)