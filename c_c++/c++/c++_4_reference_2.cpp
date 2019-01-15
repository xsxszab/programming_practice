#include<iostream>

using namespace std;

int list[]={1,2,3,4,5,6};

int& set_values(int i)
{
	return list[i];
}

int main()
{
	cout<<list[2]<<endl;
	set_values(2)=20;
	cout<<list[2]<<endl;
	return 0;
}
