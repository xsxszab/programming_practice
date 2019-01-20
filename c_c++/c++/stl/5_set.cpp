#include<iostream>
#include<set>

using namespace std;

int main()
{
	int i;
	set<int> s;
	cout<<s.empty()<<endl;
	for(i=1;i<10;i++)
		s.insert(i);
	cout<<s.size()<<endl;
	cout<<s.max_size()<<endl;
	cout<<*s.begin()<<endl;
	cout<<*s.end()<<endl;
	s.insert(2);
	cout<<s.size()<<endl;
	cout<<s.count(2)<<endl;
	set<int>::iterator p;
	p=s.find(6);
	cout<<*p<<endl;
	return 0;
}
