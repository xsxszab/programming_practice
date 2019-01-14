#include<iostream>

using namespace std;

class Box
{
	public:
		double length;
		friend void printWidth( Box box );
		void setWidth( double wid );
	private:
		double width;
};

void Box::setWidth( double wid )
{
    width = wid;
}

void printWidth( Box box )
{
   cout << "Width of box : " << box.width <<endl;
}

int main()
{
	Box box;
	box.setWidth(2.0);
	printWidth(box);
	return 0;
}
