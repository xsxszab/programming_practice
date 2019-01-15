#include<stdio.h>

int main()
{
	#define MAX 100
	printf("%d\n",MAX);
	#undef MAX
	int MAX=10;
	printf("%d\n",MAX);
	return 0;
}
