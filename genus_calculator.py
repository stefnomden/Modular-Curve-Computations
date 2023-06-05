def eulerphi(n): #takes integer n and returns phi(n), the euler totient function
  coprime = []
  for i in range(1,n+1):
    if math.gcd(i,n) == 1:
      coprime.append(i)
  return int(len(coprime))

def prime_decomp(n): #takes an integer n and returns array with power and order of primes dividing n.
  p = []
  if n < 0:
    p.append(-1)
    n = abs(n)
  i = 2
  while i*i <= n:   #prime divisors of n do not exceed the square root of n
    if n % i != 0:
      i += 1
    else:
      p.append(i) #if n is divisible by i then add i to the list of divisors, divide n by this number and start at i = 2 again.
      n = int(n/i)
      i = 2
  if n > 1:   #if the last prime was not caught by the above then n>1 and we add it to the list
    p.append(n)
  return p

def cusps(N): #takes N and returns the amount of cusps of X0(N) using the formula in section 3.8 from Diamond and Shurman's book
  divisors = []
  for i in range(1,N+1):
    if N % i == 0:
      divisors.append(i)

  sum = 0 

  for d in divisors:
    sum += eulerphi(math.gcd(d,int(N/d)))

  return sum

def period2(N): #takes N and returns the amount of elliptic points with period 2 of X0(N) using 
  if N % 4 == 0:  #the formula Corollary 3.7.2 from Diamond and Shurman's book
    return 0
  p_list = list(dict.fromkeys(prime_decomp(N)))
  prod = 1
  for p in p_list:
    symbol = 0
    if p % 4 == 1:
      symbol = 1
    if p % 4 == 3:
      symbol = -1
    prod *= 1+symbol
  return prod

def period3(N): #takes N and returns the amount of elliptic points with period 3 of X0(N) using 
  if N % 9 == 0: #the formula Corollary 3.7.2 from Diamond and Shurman's book
    return 0
  p_list = list(dict.fromkeys(prime_decomp(N)))
  prod = 1
  for p in p_list:
    symbol = 0 
    if p % 3 == 1:
      symbol = 1
    if p % 3 == 2:
      symbol = -1
    prod *= 1+symbol
  return prod

def degree(N): #takes N and returns the degree of the projection map of X0(N) using the formula 
  p_list = list(dict.fromkeys(prime_decomp(N))) #in section 3.9 from Diamond and Shurman's book
  prod = 1
  for p in p_list:
    prod *= 1 - 1/(p**2)
  return prod*(N**2)/eulerphi(N)

def genus(N): #takes N and returns the genus of X0(N) using Theorem 3.1.1 from Diamond and Shurman's book
  return int(1 + degree(N)/12 - period2(N)/4 - period3(N)/3 - cusps(N)/2)
