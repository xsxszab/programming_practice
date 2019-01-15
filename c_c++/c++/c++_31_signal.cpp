#include<iostream>
#include<csignal>
#include<cstdlib>

using namespace std;

void signalHandler(int signum)
{
	cout<<signum<<endl;
	exit(signum);  
}

int main()
{
	int i=1;
	signal(SIGINT,signalHandler);
	while(i++)
	{
		cout<<i<<endl;
		if(i==3)
			raise(SIGINT);
	}
	return 0;
}
