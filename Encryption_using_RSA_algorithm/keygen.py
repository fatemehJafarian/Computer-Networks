import random

def IsPrime(num):
  for i in range(2, num):
    if num % i == 0:
      return False
  return True

def Generate_e(phi):
  while True:
    e = random.randint(2, phi)
    if IsPrime(e):
      return e

def Generate_d(phi, e):
  a = e
  b = phi
  x = 0 
  y = 1
  while True:
    if a == 1:
      return y
    q = b // a
    b, x = (b - a*q), (x + q*y)
    if b == 1:
      return phi - x
    q = a // b
    a, y = (a - b*q), (y + q*x)

def Write_in_File(d, e, n):
  try:
      f = open('private.key', 'w')
      f.write(repr(d) + '\n')
      f.write(repr(n))
  except:
      pass
  finally:
      f.close()
  try:
      f = open('public.key', 'w')
      f.write(repr(e) + '\n')
      f.write(repr(n))
  except:
      pass
  finally:
      f.close()

P, Q = input("Enter 2 prime nums:\n").split(" ")
P = int(P)
Q = int(Q)
if IsPrime(P) and IsPrime(Q) and (P != Q):
  n = P * Q
  if n >= 256:
    Phi_n = (P - 1) * (Q - 1)
    e = Generate_e(Phi_n)
    d = Generate_d(Phi_n, e)
    out = [P, Q, n, Phi_n, e, d]
    for o in out:
      print(o)
    Write_in_File(d, e, n)
  else:
    print("P * Q is less than 256!")
elif P == Q:
  print("Numbers should be different.")
else:
  print("Both Numbers should be prime.")