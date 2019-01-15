#include<iostream>

using namespace std;

class num
{
	public:
		num(int n)
		{
			cout<<"object created"<<endl;
			number=n;
		}
		void print()
		{
			cout<<number<<endl;
		}
	private:
		int number;
};

int main()
{
	num num1(2);
	num *p;
	p=&num1;
	p->print();
	return 0;
}
