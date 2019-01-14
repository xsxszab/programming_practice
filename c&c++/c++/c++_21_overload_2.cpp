#include<iostream>

using namespace std;

class num
{
	public:
		void getnum(int n)
		{
			this->number=n;
		}
		num operator+(const num& b)
		{
			num temp;
			temp.number=this->number+b.number;
			return temp;
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
	num num2;
	num1.getnum(2);
	num2.getnum(4);
	num num3;
	num3=num1+num2;
	num3.print();
	return 0;
}
