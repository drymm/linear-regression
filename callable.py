import sys

def main(lr):

	w1=2.00057517
	w2=-3.00413686
	b=4.97633967

	x=float(sys.argv[1])
	y=float(sys.argv[2])

	if not isinstance(x, float) or not isinstance(y, float):
            raise TypeError("x and y must be type float")

	output = x*w1 - y*w2 + b
	print(output)
	return output

if __name__ == '__main__':
	main(sys.argv)