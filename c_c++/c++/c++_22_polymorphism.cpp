#include<iostream>

using namespace std;

class A
{
	public:
		A(int m,int n)
		{
			a=m;
			b=n;
		}
		virtual void print() = 0;
	protected:
		int a,b;
	
};

class B:public A
{
	public:
		B(int a=0,int b=0):A(a,b)
		{
		}
		void print()
		{
			cout<<a*b<<endl;
		}
};

class C:public A
{
	public:
	C(int a=0,int b=0):A(a,b)
		{
		}
		void print()
		{
			cout<<(a*b)/2<<endl;
		}
};

int main()
{
	//worng: A a;
	B b(2,4);
	C c(2,4);
	b.print();
	c.print();
	return 0;
}
