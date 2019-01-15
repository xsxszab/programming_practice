#include<stdio.h>

int main()
{
	printf("%d\n",7<<1>>2^2);
	printf("%d\n",(7<<1)>>2^2);
	printf("%d\n",((7<<1)>>2)^2);
	printf("%d\n",7<<1>>(2^2));
	printf("------------\n");
	printf("%d\n%d\n",NULL,EOF);
	return 0;	
}
