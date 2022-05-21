n = int(input())
n1, n2 = 0, 1 
i = 0 
if n == 1:
  print(n)
  print(n1)
else:
  for i in range(n):
      print(n1,end=' ')
      sum = n1 + n2
      n1 = n2
      n2 = sum
      i += 1