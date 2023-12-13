keep = True
while(keep):
  a,b = map(int, input().split())
  if(a == 0 and b == 0):
    keep = False
  else:
      print(a+b)