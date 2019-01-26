#include<iostream>
#include<fstream>

using namespace std;

int main()
{
	ofstream file("text.txt");
	if(file.is_open())
	{
		file<<"hello world!"<<endl;
		file.close();
	}
	ifstream read("text.txt");
	cout<<read<<endl;
	return 0;
}
