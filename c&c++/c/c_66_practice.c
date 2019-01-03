#include<stdio.h>

int a=1;
//auto int b=2;
extern int c=3;
static int d=4;

int main()
{
	printf("%d\n%d\n%d\n",a,c,d);
	return 0;
}
