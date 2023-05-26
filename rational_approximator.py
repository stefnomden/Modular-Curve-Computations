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



def rational_approximation(alpha, denom): #alpha is the real number that needs approximation, denom is the minimum size denominator
  a0 = math.floor(alpha)
  alpha1 = 1/(alpha - a0)
  a1 = math.floor(alpha1)
  q = [1, a1]
  p = [a0, a0*a1+1]
  while q[-1] <= denom and p[-1]/q[-1] != alpha:
    alphak_plus_1 = 1/(alpha1 - a1)
    ak_plus_1 = math.floor(alphak_plus_1)
    q.append(ak_plus_1*q[-1] + q[-2])
    p.append(ak_plus_1*p[-1]+p[-2])
    alpha1 = alphak_plus_1
    a1 = ak_plus_1
  return p,q
