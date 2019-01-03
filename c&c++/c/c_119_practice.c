#include<stdio.h>

int main()
{
	int a=-1;
	unsigned int b=10;
	printf("%d\n",a>b);
	printf("%d\n",a+b);
	a=(unsigned int)a;
	printf("%d\n",a+b);
	return 0;
}
