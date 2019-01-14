#include<iostream>

using namespace std;

inline int add(int a,int b)
{
	return a+b;
}

int main()
{
	cout<<add(1,2)<<endl;
	cout<<add(2,4)<<endl;
	return 0;
}
