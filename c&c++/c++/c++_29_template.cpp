#include<iostream>

using namespace std;

template <class T>
class A
{
	public:
		A()
		{
			cout<<"object created"<<endl;
		}
		T func(T a,T b)
		{
			return a+b;
		}
};

int main()
{
	A<int> a;
	cout<<a.func(2,4)<<endl;
	return 0;
}
