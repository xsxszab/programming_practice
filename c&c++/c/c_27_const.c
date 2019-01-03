#include<stdio.h>

int main()
{
	const int a=1;
	const int* p1=&a;
	const int* const p2=&a;
	printf("%d\n",a);
	printf("%d\n",*p1);
	printf("%d\n",*p2);
	return 0;
}
