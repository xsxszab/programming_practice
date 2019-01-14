#include<iostream>
#include<ctime>

using namespace std;

int main()
{
	time_t now = time(0);
	char* dt = ctime(&now);
	cout<<dt<<endl;
	tm *gmtm=gmtime(&now);
	dt=asctime(gmtm);
	cout<<dt<<endl;
	return 0;
}
