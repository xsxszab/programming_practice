#include<stdio.h>

int matrix[2][3]={0};

void print()
{
	int i,j;
	for(i=0;i<2;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("%d ",matrix[i][j]);
		}
		printf("\n");
	}
}

int main()
{
	int i,j;
	for(i=0;i<2;i++)
		for(j=0;j<3;j++)
			scanf("%d",&matrix[i][j]);
	print();
	printf("--------------\n");
	int *p=&matrix;
	*p=100;
	print();
	return 0;
}
