#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main()
{
	int i;
	srand((int)time(0));
	for(i=0;i<10;i++)
		printf("%d\n",rand()%10);
	return 0;
}
