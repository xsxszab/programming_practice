#include<stdio.h>

int main()
{
	int a=2;
	int *p1=&a;
	int **p2=&p1;
	printf("%d\n%d\n",p1,p2);
	printf("%d\n%d\n%d\n",a,*p1,**p2);
	return 0;
}
