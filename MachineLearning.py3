#python 3.6

x = [0, 1, 2, 3] 
#features
y = [1, 3, 5, 7]
#labels
w = [0, 0]
#weights
#equation: f(x) = w[0] + w[1] * x
l = 0.1
#learning rate
n = len(x)
print(n)
#number of features

def f(i):
	'''linear equation / function'''
	return w[1] * x[i] + w[0]

def mse(i):
	'''mean squared error'''
	return (f(i) - y[i]) ** 2 / (2 * n)

def dmse_df(i):
	'''derivative of mean squared error relative to linear equation'''
	return 1/n * (f(i) - y[i])

def df_dw1(i):
	'''derivative of linear equation with respect to weight 1'''
	return x[i]

def df_dw0(i):
	'''derivative of linear equation with respect to weight 0'''
	return 1

for j in range(20):
	print("Eq: " + str(w[1]) + "x + " + str(w[0]))
	print("Cost: " + str(sum(mse(i) for i in range(n))))
	print("---")
	dw0 = sum(dmse_df(i) * df_dw0(i) for i in range(n))
	dw1 = sum(dmse_df(i) * df_dw1(i) for i in range(n))
	w[0] = w[0] - l * dw0
	w[1] = w[1] - l * dw1
	