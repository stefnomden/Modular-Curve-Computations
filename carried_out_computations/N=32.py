eta_product32 = np.array([1, 0, 0, 0, -2, 0, 0, 0, -3, 0, 0, 0, 6, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 
                          0, -1, 0, 0, 0, -10, 0, 0, 0, 0, 0, 0, 0, -2, 0, 0, 0, 10, 0, 0, 0, 6, 
                          0, 0, 0, -7, 0, 0, 0, 14, 0, 0, 0, 0, 0, 0, 0, -10, 0, 0, 0, -12, 0, 0, 
                          0, 0, 0, 0, 0, -6, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, -4, 0, 0, 0, 10, 0, 
                          0, 0, 0, 0, 0, 0, 18])
M = np.array([[13,1],[64,5]])
vplus = np.array([-1,1])
vminus = np.array([1,1])
gamma = np.array([1,0])
values = coeffs_calculator(eta_product32, M, vplus, vminus, gamma)
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
