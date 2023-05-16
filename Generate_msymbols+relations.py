import math 

def coprimes_up_to(N): #returns a list containing all positive integers <= N that are coprime to N
  values = []
  for i in range(1,N+1):
    if math.gcd(i,N) == 1:
      values.append(i)
  return values

def not_coprime_up_to(N): #returns a list containing all positive integers <= N that are not coprime to N
  values = []
  for i in range(1,N+1):
    if math.gcd(i,N) > 1:
      values.append(i)
  return values

def generate_M_symbols(N): #returns a list containing all inequivalent M-symbols for N. The M symbol (c:d) has the form [c,d] in this list.
  elements = []

  for n in range(1,N+1):                    #create the set of elements where the equivalence is defined.
    for m in range(1,N+1):
      if math.gcd(math.gcd(m,n),N) == 1:
        elements.append([m,n])

  remove = []

  for i in range(0,len(elements)):          #check which elements are equivalent and add them to the elements that are to be removed
    for j in range(i,len(elements)):
      if elements[i][0]*elements[j][1] % N == elements[j][0]*elements[i][1] % N and i != j:
        remove.append(elements[j])

  for r in remove:    #remove the equivalent elements
    if r in elements:
      elements.remove(r)

  return elements


def representative(representatives, element, N): #takes list of representatives, usually generate_M_symbols(N), and an element [c,d] representing (c:d).
  for M in representatives:                      #returns the element in the representatives to which (c:d) is equivalent
    if (M[0]*element[1]) % N == (M[1]*element[0]) % N:
      return M


def two_term_relations(N): #takes a positive integer N and returns a list with all relations of the form [c,d] + [-d,c] = 0 as a string
  relations = []
  done = []
  representatives = generate_M_symbols(N)
  for M in representatives:
    if M not in done: #check for duplicates
      relations.append('{} + {} = 0'.format(M,representative(representatives, [-M[1],M[0]], N)))
      done.append(M)
      done.append(representative(representatives, [-M[1],M[0]], N))
  return relations

def three_term_relations(N): #takes a positive integer N and returns a list with all relations of the form [c,d]+[c+d,-c]+[d:-c-d] = 0 as a string
  relations = []
  done = []
  representatives = generate_M_symbols(N)
  for M in representatives:
    if M not in done:
      relations.append('{} + {} + {} = 0'.format(M, representative(representatives, [M[0]+M[1], -M[0]], N), 
                                               representative(representatives, [M[1], -M[0]-M[1]], N)))
      done.append(M)
      done.append(representative(representatives, [M[0]+M[1], -M[0]], N))
      done.append(representative(representatives, [M[1], -M[0]-M[1]], N))
  return relations
