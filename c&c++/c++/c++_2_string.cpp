#include<iostream>
#include<string>

using namespace std;

int main()
{
	string str1="abcdef";
	string str2="123456";
	string str3;
	cout<<str1+"\n"+str2<<endl;
	str3=str1;
	cout<<str3<<endl;
	str3=str1+str2;
	cout<<str3<<endl;
	int len=str3.size();
	cout<<len<<endl;
	return 0;
}
