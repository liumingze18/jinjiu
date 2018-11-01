a=1
while a <= 9:
	b = 1
	while b <= a:
		c = a*b
		print("{}*{}={:<2}".format(a,b,c),end =" ")
		b += 1
	print("")
	a += 1
	
x=9
while x > 0:
	y = 1
	while x >= y:
		z = x*y
		print("{}*{}={:<2}".format(x,y,z),end=" ")
		y += 1
	print("")
	x -= 1