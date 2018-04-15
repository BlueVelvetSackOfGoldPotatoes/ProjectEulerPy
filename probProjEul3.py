
/* Project Euler solution to exercise 3   */

/*          Largest prime factor          */

/* As written by Gonçalo Hora de Carvalho */
/* 16-04-18, Groningen Netherlands        */

n = 600851475143

def gettingPrime(f):

	for a in range(1,f/2):
		for b in range(f/2, 0, -1):
			if b != 1 and a!=f:
				return 0
	return 1

def main():
	
	 a = n/2
	 b = a - 1
	 
	 while(a != 0): 
		 while(b != 0):
			 if a * b == n:
				 if a >= b:
					factor = gettingPrime(a)
					maxFactor = a
				 else:
					factor = gettingPrime(b)
					maxFactor = b
				
				if factor == 0:
					maxFactor = n
			 b--
		 a--
	 
	 
	print "The max prime factor is:", maxFactor
