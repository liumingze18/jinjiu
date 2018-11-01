for a in range(1,10):
	for b in range(1,a+1):
		c = a*b
		print("{}*{}={:<2}".format(a,b,c),end=" ")
	print("")

for x in range (9,0,-1):
	for y in range(1,x+1):
		z = x*y
		print("{}*{}={:<2}".format(x,y,z),end=" ")
	print("")
