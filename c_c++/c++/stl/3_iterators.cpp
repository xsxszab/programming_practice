#include<iostream>
#include<vector>

using namespace std;

int main()
{
	int i;
	vector<int> vec;
	for(i=0;i<10;i++)
		vec.push_back(i*10);
	vector<int>::iterator p;
	for(p=vec.begin();p!=vec.end();p++)
		cout<<*p<<" "<<&p<<endl;
	return 0;
}
