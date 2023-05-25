eta_product36 = np.array([1, 0, 0, 0, 0, 0, -4, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 
                          0, 8, 0, 0, 0, 0, 0, -5, 0, 0, 0, 0, 0, -4, 0, 0, 0, 
                          0, 0, -10, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 9, 0, 0, 
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 0, 0, 0, 0, 0, -16, 0, 
                          0, 0, 0, 0, -10, 0, 0, 0, 0, 0, -4, 0, 0, 0, 0, 0, 0, 0, 
                          0, 0, 0, 0, -8, 0, 0, 0, 0, 0, 14])
M = np.array([[31,2],[108,7]])
vplus = np.array([0,1])
vminus = np.array([-2,1])
gamma = np.array([1,1])
expected_j = 0
values = coeffs_calculator(eta_product36, M, vplus, vminus, gamma)
print('ω1=',values[3])
print('ω2=',values[4])
print('ω1/ω2=',values[3]/values[4])
print('g4=', values[0])
print('g6=', values[1])
c4 = 12*values[0]/((2*math.pi)**4)
c6 = -216*values[1]/((2*math.pi)**6)
c4guess = round(c4.real)
c6guess = round(c6.real)
print('c4guess=',c4guess)
print('c6guess=',c6guess)
u = u_calculator(c4guess, c6guess)
print('u=',u)
c4prime = c4guess/(u**4)
c6prime = c6guess/(u**6)
a = a_calculator(c4prime, c6prime)
print('coeffs:',a)
print('j=', values[2])
print('expected j=',expected_j)
print('error=',abs(expected_j-values[2]))
