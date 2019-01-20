#include<iostream>
#include<stack>

using namespace std;

int main()
{
	int i;
	stack<int> s;
	for(i=0;i<10;i++)
		s.push(i*10);
	cout<<s.size()<<endl;
	s.pop();
	cout<<s.size()<<endl;
	cout<<s.top()<<endl;
	cout<<s.size()<<endl;
	cout<<s.empty()<<endl;
	return 0;
}
