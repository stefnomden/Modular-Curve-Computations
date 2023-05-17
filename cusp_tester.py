import math

def equiv_test(p1,q1,p2,q2,N):  #pi, qi are such that pi/qi in lowest terms. qi can be 0 and this value of qi represents ∞
  uvalues = []                   #returns whether p1/q1 and p2/q2 are equivalent cusps in X(\Gamma_0(N))
  for u in range(1, N):          #Uses Proposition 2.2.3. from Cremora
    if math.gcd(u, N) == 1:
      uvalues.append(u)

  for u in uvalues:
    if (q2 % N) == ((u*q1) % N) and ((u*p2) % math.gcd(q1,N)) == (p1 % math.gcd(q1,N)):
      return '{}/{} and {}/{} are equivalent cusps of Γ0({})'.format(p1,q1,p2,q2,N)
  return '{}/{} and {}/{} are NOT equivalent cusps of Γ0({})'.format(p1,q1,p2,q2,N)
