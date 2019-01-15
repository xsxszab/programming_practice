#include<stdio.h>
#include<stdlib.h>

int main()
{
	int *p1=NULL;
	int *p2;
	void* p3=malloc(2);
	printf("%d\n%d\n%d\n",p1,p2,p3);
	return 0;
}
