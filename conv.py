def priority(c):
	if c == '+' or c == '-':
		return 0;
	if c == '*' or c == '/':
		return 1;
	else:
		return 2;

def conv(expr):
	ops = []
	i  = 0;
	ans = []

	for i in range(len(expr)):
		if type(expr[i]) == float:
			ans.append(expr[i]);
		if expr[i] == '(':
			ops.append('(');
		if expr[i] == ')':
			while(ops[-1] != '('):
				temp = ops.pop();
				ans.append(temp);
				if(len(ops)== 0):
					print 'error';
					return float("NaN");
			ops.pop();
		if expr[i] == '+' or expr[i] == '-' or expr[i] == '*' or expr[i] == '/':
			while(len(ops) > 0 and priority(ops[-1]) >= priority(expr[i])):
				temp = ops.pop();
				ans.append(temp);
			ops.append(expr[i]);
	while(len(ops) > 0):
		temp = ops.pop();
		ans.append(temp);


	return ans;
