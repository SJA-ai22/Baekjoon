dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
sen = input()
result = 0

for j in range(len(sen)):
    for i in dial:
        if sen[j] in i:
            result += dial.index(i)+3

print(result)