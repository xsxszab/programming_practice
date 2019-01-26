#include<iostream>

using namespace std;

unsigned long hash(string key)
{
	unsigned int i;
	unsigned long value=0;
	for(i=0;i<key.size();i++)
	{
		value=value*33+key[i];
	}
	return value;
}

int main()
{
	string key;
	cin>>key;
	cout<<hash(key)<<endl;
	return 0;
}
