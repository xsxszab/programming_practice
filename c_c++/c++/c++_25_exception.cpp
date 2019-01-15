#include<iostream>

using namespace std;

double division(double a,double b)
{
	if(b==0)
		throw "division by zero";
	return a/b;
}

int main()
{
	double a=12.34;
	double ans;
	cout<<division(a,1.0)<<endl;
	try
	{
		ans=division(a,0);
		cout<<ans<<endl;
	}catch(const char* msg)
	{
		cerr<<msg<<endl;
	}
	return 0;
}
