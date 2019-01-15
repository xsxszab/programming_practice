#include<iostream>

using namespace std;

class num
{
	public:
		num()
		{
			number=2;
		}
		num(int n)
		{
			number=n;
		}
		num operator-()
		{
			number=-number;
			return num(number);
		}
		void print()
		{
			cout<<this->number<<endl;
		}
	private:
		int number;
};

int main()
{
	num num1;
	num1.print();
	-num1;
	num1.print();
	return 0;
}
