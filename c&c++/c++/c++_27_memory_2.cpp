#include<iostream>

using namespace std;

class num
{
	public:
	num()
	{
		cout<<"object created"<<endl;
	}
	~num()
	{
		cout<<"object deleted"<<endl;
	}
};

int main()
{
	int *array=new int [10];
	delete [] array;
	num* num1=new num[20];
	delete [] num1;
	return 0;
}
