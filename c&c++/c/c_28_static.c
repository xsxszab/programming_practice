#include<stdio.h>

void func()
{
	static int a=2;
	printf("%d\n",a);
	a++;
}

int main()
{
	int i;
	for(i=0;i<10;i++)
		func();
	return 0;
}
