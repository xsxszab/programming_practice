#include<iostream>

using namespace std;

class rec
{
	public:
		int length;
		int height;
};

int main()
{
	rec rec1;
	rec1.length=2;
	rec1.height=4;
	cout<<rec1.length<<endl;
	cout<<rec1.height<<endl;
	return 0;
}
