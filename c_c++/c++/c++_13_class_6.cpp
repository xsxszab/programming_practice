#include<iostream>

using namespace std;

class num
{
	public:
		num(int n)
		{
			cout<<"object created"<<endl;
			ptr=new int;
			*ptr=n;
		}
		num(const num &obj)
		{
			ptr=new int;
			*ptr=*obj.ptr;
		}
		~num()
		{
			delete ptr;
			cout<<"object deleted"<<endl;
		}
	private:
		int *ptr;
};

int main()
{
	num num1(2);
	num num2=num1;
	return 0;
}
