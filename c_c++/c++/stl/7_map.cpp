#include<iostream>
#include<utility>
#include<map>

using namespace std;

int main()
{
	typedef pair<int,string> stu;
	map<int,string> map1;
	map1.insert(stu(1,"a"));
	map1.insert(stu(2,"b"));
	map1.insert(map<int,string>::value_type(3,"c"));
	cout<<map1.size()<<endl;
	return 0;
}
