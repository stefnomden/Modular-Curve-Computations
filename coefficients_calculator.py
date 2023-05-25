#the functions in this file are implementations of the Kraus–Laska–Connell
#algorithm which can be found in section 3.2 of Cremona's book 'Algorithms for Modular Elliptic Curves'


def mod(n,p):         #takes integers n and p and returns n mod p between -p/2 and p/2
  modulo = n % p      
  if modulo > 0.5*p:
    return modulo - p
  else: 
    return modulo

def ord(p,n):       #takes n and a prime divisor p of n and returns alpha where alpha 
  alpha = 0         #is the biggest integer such that p^alpha divides n
  if p == n:
    return 1
  while n % p == 0:
    alpha += 1
    n = int(n/p)
  return alpha


def u_calculator(c4,c6):     #takes integers c4, c6 and calculates u to reduce these coefficients
  delta = np.float128(((c4)**3 - (c6)**2)/1728)
  u = 1
  g = math.gcd(c6**2,int(delta))
  p_list = list(dict.fromkeys(prime_decomp(g)))
  for p in p_list:
    d = math.floor(ord(p,g)/12)
    if p == 2:
      a = mod(c4/(2**(4*d)),16)
      b = mod(c6/(2**(6*d)),32)
      if mod(b,4) != -1 and not (a==0 and (b==0 or b==8)):
        d = d - 1
    if p == 3:
      if ord(3,c6) == 6*d+2:
        d = d - 1
    u = u*(p**d)
  return u


def a_calculator(c4,c6):    #takes reduced coefficients c4 and c6, returns 
  b_2 = -c6 % 12            #coefficients a_i for the reduced weierstrass equation
  if b_2 > 6:
    b_2 -= 12

  b_4 = (b_2**2-c4)/24
  b_6 = (-(b_2)**3 + 36*b_2*b_4 - c6)/216
  a_1 = b_2 % 2
  a_3 = b_6 % 2
  a_2 = (b_2-a_1)/4
  a_4 = (b_4 - a_1*a_3)/2
  a_6 = (b_6-a_3)/4

  return a_1,a_3,a_2,a_4,a_6
