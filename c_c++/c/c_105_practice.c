#include<stdio.h>

int main()
{
	char c;
	while(scanf("%c",&c)!=EOF)
	{
		printf("----------\n%c: %d\n----------\n",c,c);
		getchar();
	}
	return 0;
}
