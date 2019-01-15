#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main()
{
	int i;
	for(i=0;i<10;i++)
		printf("%d\n",rand()%10);
	printf("-----------------\n");
	srand(1);
	for(i=0;i<10;i++)
		printf("%d\n",rand()%10);
	printf("-----------------\n");
	srand(2);
	for(i=0;i<10;i++)
		printf("%d\n",rand()%10);
	return 0;
}
