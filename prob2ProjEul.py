sumz = 0
term = 1
nexTerm = 2
anotherTerm = 1+2
  
while term <= 4000000:
  if anotherTerm % 2 == 0:
    sumz = sumz + anotherTerm
    
   term = nexTerm
   nexTerm = anotherTerm
   anotherTerm = term + nexTerm
	
print(sumz)
