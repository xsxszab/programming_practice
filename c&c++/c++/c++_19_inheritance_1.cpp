#include<iostream>

using namespace std;

class A
{
	public:
		A()
		{
			cout<<"A"<<endl;
		}
		void getnum(int m,int n)
		{
			a=m,b=n;
		}
	protected:
		int a,b;
};

class B: public A
{
	public:
		void print()
		{
			cout<<a*b<<endl;
		}
};

int main()
{
	B b;
	b.getnum(2,4);
	b.print();
	return 0;
}
