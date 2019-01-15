#include<iostream>

using namespace std;

class num
{
	public:
		num(int n):number(n)
		{
			cout<<"object created"<<endl;
		}
		~num()
		{
			cout<<number<<endl;
			cout<<"object deleted"<<endl;
		}
	private:
		int number;
};

int main()
{
	num num1(2);
	return 0;
}
