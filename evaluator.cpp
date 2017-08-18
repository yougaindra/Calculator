#include <iostream>
#include <cstdio>
#include <stack>

int priority(char);

std::string eval(std::string expr)
{
	std::stack<char> ops;
	std::string ans;
	int i = 0;

	
	while(i < expr.length())
	{
		//printf("%d\n",expr[i]);
		if((char)expr[i] == ' ')
		{
			i++;
			//std::cout << "wtf";
		}

		else
		if(expr[i] == '(')
		{
			ops.push('(');
			i++;
		}

		else
		if(expr[i] == ')')
		{
			while(ops.top() != '(' && !ops.empty())
			{
				char temp = ops.top();
				ops.pop();
				ans += temp;
				i++;
			}

			if(ops.empty())
			{
				return "Invalid Expression";
				
			}

			ops.pop();
		}

        else 
        if(expr[i]=='+'||expr[i]=='-'||expr[i]=='*'||expr[i]=='/'||expr[i]=='%'||expr[i]=='^')
        {
        	while((ops.empty() == 0) && (ops.top() != '(') && (priority(ops.top()) > priority(expr[i])))
        	{
        		ans += ops.top();
        		ops.pop();
        	}

        	ops.push(expr[i]);
        	i++;
        }

        else
        {
        	ans += expr[i];
        	i++;
        }

	}

	while(!ops.empty() && ops.top() != '(')
	{
		ans += ops.top();
		ops.pop();
	}

	return ans;

} 


int priority(char op)
{
	if(op == '+' || op == '-')
		return 0;
	if(op == '/' || op == '*')
		return 1;
	else
		return 2;
}
