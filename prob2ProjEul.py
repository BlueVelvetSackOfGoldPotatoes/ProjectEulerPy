sumz = 0
term = 1
nexTerm = 2
  
while term <= 4000000:
  if term % 2 == 0:
    sumz = sumz + term
    
    term = nexTerm
    nexTerm = nexTerm + term
	
print(sumz)
