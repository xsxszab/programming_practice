#include<stdio.h>

int main()
{
	int n;
	n=(1,2,3);
	printf("%d\n",n);
	int a,b,c;
	c=(a=20,b=9,a=a+1);
	printf("%d\n",c);
	return 0;
}
