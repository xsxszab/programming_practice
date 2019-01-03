#include<stdio.h>

int main()
{
	int a=1;
	int b=2;
	{
		int c=3;
		int d=4;
		printf("%d\n%d\n",c,d);
	}
	printf("%d\n%d\n",a,b);
	//error: printf("%d\n%d\n",c,d);
	return 0;
}
