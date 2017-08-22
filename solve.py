import conv
import inp
def evaluate(s):
	expression = s;
	expression = inp.inp(expression);
	expression = conv.conv(expression);
	return inp.eval(expression);
