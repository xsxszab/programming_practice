#include<iostream>

using namespace std;

class num
{
	public:
		static int count;
		num(int n)
		{
			cout<<"object created"<<endl;
			number=n;
			count++;
		}
	private:
		int number;
};

int num::count=0;

int main()
{
	num num1(2);
	num num2(4);
	cout<<num::count<<endl;
	return 0;
}
