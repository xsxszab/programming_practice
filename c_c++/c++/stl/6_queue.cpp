#include<iostream>
#include<queue>

using namespace std;

int main()
{
	int i;
	queue<int> list;
	for(i=0;i<10;i++)
		list.push(i*10);
	cout<<list.size()<<endl;
	cout<<list.back()<<endl;
	cout<<list.front()<<endl;
	list.pop();
	cout<<list.back()<<endl;
	cout<<list.front()<<endl;
	cout<<list.empty()<<endl;
	return 0;
}
