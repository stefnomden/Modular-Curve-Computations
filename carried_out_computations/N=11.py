eta_product11 = np.array([1,-2,-1,2,1,2,-2,0,-2,-2,1,-2,4,4,-1,-4,-2,4,0,2,2,-2,-1,0,-4,-8,5,-4,0,2,7,8,-1,4,-2,-4,3,0,-4,0,
                     -8,-4,-6,2,-2,2,8,4,-3,8,2,8,-6,-10,1,0,0,0,5,-2,12,-14,4,-8,4,2,-7,-4,1,4,-3,0,4,-6,4,0,-2,8,-10,
                     -4,1,16,-6,4,-2,12,0,0,15,4,-8,-2,-7,-16,0,-8,-7,6,2])
M = np.array([[4,1],[11,3]])
vplus = np.array([2,1])
vminus = np.array([0,1])
gamma = np.array([0,1])
values = coeffs_calculator(eta_product11, M, vplus, vminus, gamma)
print('ε(M)=', values[5])
print('ω1=',values[3])
print('ω2=',values[4])
print('g4=', values[0])
print('g6=', values[1])
print('error4=', values[6])
print('error6=', values[7])
c4 = 12*values[0]
c6 = 216*values[1]
c4guess = round(c4.real)
c6guess = round(c6.real)
print('c4guess=',c4guess)
print('c6guess=',c6guess)
u = u_calculator(c4guess, c6guess)
c4prime = c4guess/(u**4)
c6prime = c6guess/(u**6)
a = a_calculator(c4prime, c6prime)
delta = (c4prime**3 - c6prime**2)/1728
expected_j = (c4prime**3)/delta
print('coeffs:',a)                    #order is (a_1,a_3,a_2,a_4,a_6)
print('Δ=',delta,'=',prime_decomp(delta))
print('j=', values[2])
print('expected j=',expected_j)
print('error=',abs(expected_j-values[2]))
