#include<iostream>

using namespace std;

int add(int& a,int& b)
{
	int ans;
	ans=a+b;
	return ans;
}

int main()
{
	int a=20;
	int &r1=a;
	cout<<a<<endl;
	cout<<r1<<endl;
	int b=2;
	int &r2=b;
	cout<<add(r1,r2)<<endl;
	return 0;
}
