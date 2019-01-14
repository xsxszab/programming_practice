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
		void compare(num temp)
		{
			cout<<(this->number>=temp.number)<<endl;
		}
	private:
		int number;
};

int main()
{
	num num1(4);
	num num2(2);
	num1.compare(num2);
	num2.compare(num1);
	return 0;
}
