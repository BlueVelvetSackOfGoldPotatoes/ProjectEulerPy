# Project Euler solution to exercise 1

#          Multiples of 3 and 5

# As written by Gonçalo Hora de Carvalho
# 24-12-17, Groningen Netherlands

sumz = 0
for i in range(0, 1000):
		if i % 3 == 0 or i % 5 == 0:
		 sumz = sumz + i
print(sumz)
	
