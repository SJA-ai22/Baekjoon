def is_prime(a):
    if a <= 1:
      return False
    for i in range(2, int(a**0.5)+1):
      if a % i == 0:
        return False
    return True

def find_next_prime(num):
    if num <= 1:
        return 2
    while True:
        if is_prime(num) == False:
          num+=1
        else:
          break
    return num

n = int(input())
results = []

for i in range(n):
    num = int(input())
    next_prime = find_next_prime(num)
    results.append(next_prime)

for result in results:
    print(result)