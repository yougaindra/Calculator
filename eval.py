

def inp(s):
	ret = []
	temp = ''
	for ind,i in enumerate(s):
		if i == '+' or i == '-' or i == '/' or i == '*' or i == '(' or i == ')':
			if(len(temp) != 0):
				ret.append(float(temp));
				temp = ''
			ret.append(i);
		elif i == ' ':
			continue;
		elif (ord(i) >= ord('0') and ord(i) <= ord('9')) or i == '.':
			temp += i

	if len(temp) != 0:
		ret.append(float(temp))

	return ret;



def eval(postfix):
	stk = []
	for i in postfix:
		if type(i) == float:
			stk.append(i);
		else:
			if len(stk) < 2:
				print 'error';
				return float('NaN');
			op1 = stk.pop()
			op2 = stk.pop()
			if i == '+':
				stk.append(op1+op2);
			elif i == '-':
				stk.append(op1-op2);
			elif i == '*':
				stk.append(op1*op2);
			elif i == '/':
				stk.append(op1/op2);
			elif i == '%':
				stk.append(op1%op2);

	return stk[-1]
