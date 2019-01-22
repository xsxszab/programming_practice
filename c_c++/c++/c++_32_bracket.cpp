#include<iostream>
#include<stack>

using namespace std;

int main()
{
	int i=0;
	int flag=0;
	stack<char> list;
	string str;
	cin>>str;
	int len=str.size();
	while(i<len)
	{
		if(str[i]=='('||str[i]=='['||str[i]=='{')
		{
			flag=1;
			list.push(str[i]);
		}
		if(str[i]==')')
		{
			if(list.top()=='(')
				list.pop();
			else
			{
				cout<<"wrong"<<endl;
				return 0;
			}
		}
		if(str[i]==']')
		{
			if(list.top()=='[')
				list.pop();
			else
			{
				cout<<"wrong"<<endl;
				return 0;
			}
		}
		if(str[i]=='}')
		{
			if(list.top()=='{')
				list.pop();
			else
			{
				cout<<"wrong"<<endl;
				return 0;
			}
		}
		i++;
	}
	if(list.empty()&&flag)
		cout<<"right"<<endl;
	else
		cout<<"wrong"<<endl;
	return 0;
}
