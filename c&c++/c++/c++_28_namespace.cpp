#include<iostream>

using namespace std;

namespace test
{
	void print()
	{
		cout<<"hello world"<<endl;
	}
}

namespace test1
{
	namespace test2
	{
		void print()
		{
			cout<<"this is namespace test2"<<endl;
		}
	}
	void print()
	{
		cout<<"this is namespace test1"<<endl;
	}
}

int main()
{
	test::print();
	using namespace test;
	print();
	test1::print();
	using namespace test1;
	test2::print();
	return 0;
}
