#include<stdio.h>

typedef struct bitdata
{
	int a: 32;
	//wrong: int a: 33;
	char b:4;
	unsigned char c:2;
	int d: 20;
}data;

int main()
{
	data bit;
	bit.a=10;
	printf("%ld\n",sizeof(data));
	printf("%d\n",bit.a);
	return 0;
}
