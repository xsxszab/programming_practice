#include<stdio.h>

int main()
{
	int x=0,y=1,z=1;
	if(x&&y++)
		NULL;
	x=1;
	if(x||z++)
		NULL;
	printf("%d\n%d\n%d\n",x,y,z);
	return 0;
}
