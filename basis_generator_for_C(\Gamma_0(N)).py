import numpy as np 
import sympy as sp

def modulo_relations_matrix(N): #takes a postive integer N and returns a solved matrix representing the relations and every symbol [c,d] expressed in terms of basis vectors
  relations = []
  symbols = generate_M_symbols(N) #get list of representatives

  done = []
  for m in symbols:   #add the three term relations in an array of the form [[c1,d1],[c2,d2],[c3,d3]]
    if m not in done:
      relations.append([m, representative(symbols, [m[0]+m[1], -m[0]], N), representative(symbols, [m[1], -m[0]-m[1]], N)])
      done.append(m)
      done.append(representative(symbols, [m[0]+m[1], -m[0]], N))
      done.append(representative(symbols, [m[1], -m[0]-m[1]], N))

  done = []
  for m in symbols:    #add the two term relations in an array of the form [[c1,d1],[c2,d2]]
    if m not in done:
      relations.append([m, representative(symbols,[-m[1],m[0]],N)])
      done.append(m)
      done.append(representative(symbols,[-m[1],m[0]],N))

  A = np.zeros((len(relations), len(symbols))) #create matrix which will represent the linear system of relations between M-symbols. 
                                               #this matrix will be solved so that we obtain a basis for C(G)/B(G) and an expression for the other symbols
    
  for i in range(0,len(relations)): #every relation corresponds to a row, here we add a 1 in the j-th column if the j-th M-symbol is in the relation list
    for j in range(0,len(symbols)):
      for k in relations[i]:
        if symbols[j] == k:
          A[i,j] += 1
  
  rrA = np.array(sp.Matrix(A).rref()[0]).astype(int)  #puts the matrix A in reduced row echelon form and converts the entries to int

  solved = []
 
  for r in range(0,rrA.shape[0]):                     #creates a string that gives the relation in text form and puts it in list for later use
    if rrA[r].any() != np.zeros(rrA.shape[1]).astype(int).any():
      eq = ''
      for i in range(0,len(rrA[r])):
        if rrA[r,i] != 0:
          if rrA[r,i] > 0:
            eq += '+{}{} '.format(rrA[r,i], symbols[i])
          if rrA[r,i] < 0:
            eq += '{}{} '.format(rrA[r,i], symbols[i])
      eq += '= 0'
      solved.append(eq)

  return solved, rrA
