#include<iostream>

using namespace std;

template <typename T>
T add(T a,T b)
{
	return a+b;
}

int main()
{
	cout<<add(2,4)<<endl;
	return 0;
}
