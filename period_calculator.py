import cmath
import math

def g_4(w_1, w_2, R=50):  #takes generators of lattice and returns g_4
  if (w_1/w_2).imag > 0:  #formula used is equation 6.50 in Knapp
    omega_1 = w_1
    omega_2 = w_2
  else:
    omega_2 = w_1
    omega_1 = w_2

  tau = omega_1/omega_2
  print('tau', tau)
  sum = 0
  for n in range(1,R):
    sum += (n**3)/(cmath.exp(complex(0,-2*math.pi*n*tau)) - 1)
  factor = (4*(math.pi**4))/(3*(omega_2**4))
  
  return factor*(1+240*sum)

def g_6(w_1,w_2, R=50):   #takes generators of lattice and returns g_6
  if (w_1/w_2).imag > 0:  #formula used is equation 6.50 in Knapp
    omega_1 = w_1
    omega_2 = w_2
  else:
    omega_2 = w_1
    omega_1 = w_2

  tau = omega_1/omega_2
  sum = 0
  for n in range(1,R):
    sum += (n**5)/(cmath.exp(complex(0,-2*math.pi*n*tau)) - 1)
  factor = (8*(math.pi**6))/(27*(omega_2)**6)

  return factor*(1-504*sum)


def Phi_f(M, f): #M is a 2x2 matrix in \Gamma_0(N), f is an array with the fourier coefficients of f
  a = M[0,0]     #Returns the period Phi_f(M) calculated as in Proposition 2.10.2. of Cremora
  b = M[0,1]
  cN = M[1,0]
  d = M[1,1]
  sum = 0

  for n in range(1, f.shape[0]+1):
    sum += ((f[n-1])/n)*(math.e**(complex(-(2*math.pi*n)/(cN),0)))*(math.e**(complex(0,(2*math.pi*n*a)/(cN))) - math.e**(complex(0,(-2*math.pi*n*d)/(cN))))
  return sum


def coeffs_calculator(f, M, vplus, vminus, gamma): #takes array with fourier coeffs of f a 2x2 matrix M in \Gamma_0(N), two row vectors of length two vplus,vminus and a vector 
  period = Phi_f(M,f)                              #gamma. calculates a period and returns generators for the period lattice, also computes g_4, g_6 and the j-invariant of C/Λ_f
  x = period.real/(vplus[0]*gamma[0] + vplus[1]*gamma[1])
  y = period.imag/(vminus[0]*gamma[0] + vminus[1]*gamma[1])
  w_1 = complex(vplus[0]*x, vminus[0]*y)
  w_2 = complex(vplus[1]*x, vminus[1]*y)
  g4 = g_4(w_1,w_2)
  g6 = g_6(w_1,w_2)
  j = (1728*(g4**3))/(g4**3-27*(g6**2))
  error = math.e**(-2*math.pi*(f.shape[0]+1)/M[1,0])/(1-math.e**(-2*math.pi/M[1,0])) #estimated error (see section 5.3)
  return g4, g6, j, w_1, w_2, error


