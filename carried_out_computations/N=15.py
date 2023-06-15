eta_product15 = np.array([1, -1, -1, -1, 1, 1, 0, 3, 1, -1, -4, 1, -2, 0, -1, -1, 2, -1, 4, -1, 0, 4, 
                        0, -3, 1, 2, -1, 0, -2, 1, 0, -5, 4, -2, 0, -1, -10, -4, 2, 3, 10, 0, 4, 4, 
                        1, 0, 8, 1, -7, -1, -2, 2, -10, 1, -4, 0, -4, 2, -4, 1, -2, 0, 0, 7, -2, -4, 
                        12, -2, 0, 0, -8, 3, 10, 10, -1, -4, 0, -2, 0, -1, 1, -10, 12, 0, 2, -4, 2, 
                        -12, -6, -1, 0, 0, 0, -8, 4, 5, 2, 7, -4])
M = np.array([[-17,-4],[30,7]])
vplus = [0,1]
vminus = [1,0]
gamma = np.array([-1,1])
values = coeffs_calculator(eta_product15,M,vplus,vminus,gamma)
print('ε(M)=', values[5])
print('ω1=',values[3])
print('ω2=',values[4])
print('g4=', values[0])
print('g6=', values[1])
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
