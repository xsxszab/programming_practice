#include<stdio.h>

typedef struct Data
{
	int a;
	int* p;
}data;

int main()
{
	data s;
	int* p=&s.a;
	*p=2;
	int *ap[10]={0};
	return 0;
}
