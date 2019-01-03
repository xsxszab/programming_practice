#include<stdio.h>

int main()
{
	float x=1.4;
	x=x-(int)x;
	int i;
	i=(int)(x*10);
	printf("%f\n%d\n",x,i);
	i=(i*10+0.00005);
	printf("%d\n",i);
	return 0;
}
