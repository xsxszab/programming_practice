#include<stdio.h>

int main()
{
	int matrix[3][4];
	printf("%ld\n",sizeof(matrix));
	printf("-----------------\n");
	printf("%ld\n",sizeof(*matrix));
	printf("-----------------\n");
	printf("%ld\n",sizeof(&matrix));
	printf("-----------------\n");
	int *p;
	printf("%ld\n",sizeof(p));
	printf("-----------------\n");
	printf("%ld\n",sizeof(*p));
	printf("-----------------\n");
	return 0;
}
