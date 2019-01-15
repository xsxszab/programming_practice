#include<stdio.h>

int main()
{
	int a=1;
	int *b;
	void *c;
	b=&a;
	c=b;
	printf("%d\n",*(int*)c);	
	return 0;
}
