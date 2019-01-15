#include<iostream>

using namespace std;

class rec
{
	public:
		int length;
		int height;
		int get_area();
};

int rec::get_area()
{
	return length*height;
}

int main()
{
	rec rec1;
	rec1.length=2;
	rec1.height=4;
	cout<<rec1.get_area()<<endl;
	return 0;
}
