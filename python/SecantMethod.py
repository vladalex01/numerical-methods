import numpy as np
#  solves f(x) = 0 by doing max_iter steps of the secant method;
#  the secant method requires two initial values, x0 and x1
#  which should ideally be chosen close to the root;
#  y = feval(f, x)  evaluates a function using its name or its handle
#  and using the input arguments;
def f(x):
	return 2 * x**5 + 1

def SecantMethod(f, x0, x1, tol, max_iter):
	x = 0
	for i in range (1, max_iter):
		print("	La pasul: {}".format(i))
		# function values: f(x0) and f(x1)
		f0 = f(x0)
		f1 = f(x1)
		print("f0 = {}; f1 = {}".format(f0, f1))
		# the root of function f is approximated using the formula 
		xi = x1 - f1 * (x1 - x0) / (f1 - f0)
		# calculate f(xi)
		fxi = f(xi) 

		# xi is the solution
		if (abs(fxi) < np.finfo(float).eps):
			x = xi
			return x
		# calculate eps
		epsilon = abs((xi - x1) / xi)
		
		# stop if the secant method reached its convergence limit
		if (epsilon < tol):
			x = xi
			return x
		# update the last two computed values
		x0 = x1
		x1 = xi

	print("Maximum number of iterations reached: {}".format(i))	    
	return x

print(SecantMethod(f, 17.0, 6.0, 10 ** (-10), 100))