#include<stdio.h>

int main()
{
	register int a=1;
	volatile int b=2;
	auto int c=3;
	static int d=4;
	const int e=5;
	printf("%d\n%d\n%d\n%d\n%d\n",a,b,c,d,e);
	return 0;
}
