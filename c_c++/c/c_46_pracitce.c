#include<stdio.h>

typedef union datastorage
{
	int i;
	float j;
	char str[100];
} data;

int main()
{
	data a;
	printf("%ld\n",sizeof(a));
	a.i=1;
	printf("%d\n",a.i);
	a.j=0.2;
	printf("%.1f\n",a.j);
	printf("%d\n",a.i);
	return 0;
}
