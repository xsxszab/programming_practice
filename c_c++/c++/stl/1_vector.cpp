#include<iostream>
#include<vector>

using namespace std;

int main()
{
	int i;
	vector<int> vec(10);
	for(i=0;i<10;i++)
		vec[i]=i+1;
	cout<<vec.size()<<endl;
	cout<<vec.empty()<<endl;
	vec.push_back(11);
	cout<<vec.size()<<endl;
	vec.resize(20);
	cout<<vec.size()<<endl;
	vector<int> v=vec;
	cout<<(v==vec)<<endl;
	vector< vector<int> > matrix;
	vec.pop_back();
	cout<<vec.size()<<endl;
	cout<<vec[2]<<endl; 
	return 0;
}
