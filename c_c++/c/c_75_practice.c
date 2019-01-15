#include<stdio.h>

int main()
{
	int a[][3]={{1},{2,3}};
	int b[][3]={{1,2,3},{2},{}};
	//wrong:  int c[2][]={1,2,3};
	int c[][3]={1,2,3,4,5,6,7};
	return 0;
}
