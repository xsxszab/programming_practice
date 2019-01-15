#include<stdio.h>

int main()
{
	int n=10;
	n<<=1;
	printf("%d\n",n);
	n>>=2;
	printf("%d\n",n);
	printf("%d\n",2|3);
	printf("%d\n",2%3);
	printf("%d\n",2^3);
	printf("%d\n",~2);
	return 0;
}
