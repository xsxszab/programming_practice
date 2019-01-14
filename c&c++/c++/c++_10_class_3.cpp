#include<iostream>

using namespace std;

class rec
{
	private:
		int h,l;
	public:
		void set_length(int i)
		{
			l=i;
		}
		void set_height(int i)
		{
			h=i;
		}
		void print()
		{
			cout<<l<<endl;
			cout<<h<<endl;
		}
};

int main()
{
	rec rec1;
	rec1.set_length(2);
	rec1.set_height(4);
	rec1.print();
	return 0;
}
