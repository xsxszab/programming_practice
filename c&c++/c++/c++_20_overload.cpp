#include<iostream>

using namespace std;

int add(int a,int b)
{
	return a+b;
}

double add(double a,double b)
{
	return a+b;
}

int main()
{
	cout<<add(2,4)<<endl;
	cout<<add(1214.325,235.436)<<endl;
	return 0;
}
