#include<stdio.h>

int main()
{
	int p[0];
	printf("%ld\n",sizeof(p));
	printf("%ld\n",sizeof(*p));
	printf("%ld\n",sizeof(&p));
	return 0;
}
