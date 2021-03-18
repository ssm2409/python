for _ in range(int(input())):
 a,b=list(map(str,input().split()))
 
 if '.' in a:
  a=float(a)
 else:
  a=int(a)
 if '.' in b:
  b=float(b)
 else:
  b=int(b) 
 print(a+b)
