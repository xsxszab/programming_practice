#include<iostream>

using namespace std;

int main()
{
	int *p=NULL;
	p=new int;
	*p=2;
	cout<<*p<<endl;
	delete p;
	return 0;
}
