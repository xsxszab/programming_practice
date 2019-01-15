#include<stdio.h>
#include<stdlib.h>

int x=1,y=2;

void func()
{
	extern a,b;
	printf("%d %d\n",a,b);
}

int a=3,b=4;

int main()
{	
	func();
	printf("%d %d\n",x,y);
	return 0;
}
