#include<stdio.h>

int main()
{
	int n;
	while(scanf("%d",&n)!=0)
	{
		switch(n)
		{
			case 1:
				printf("1\n");
				break;
			case 2:
				printf("2\n");
				break;
			default:
				printf("not 1 or 2\n");
				break;
		}
	}
	return 0;
}
