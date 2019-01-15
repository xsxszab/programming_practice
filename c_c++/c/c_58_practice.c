#include<stdio.h>

#define N 3

int main()
{
	int i,j;
	int matrix[N][N];
	for(i=0;i<N;i++)
		for(j=0;j<N;j++)
			scanf("%d",&matrix[i][j]);
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
			printf("%d ",matrix[i][j]);
		printf("\n");
	}
	printf("-----------\n");
	for(i=0;i<N;i++)
	{
		for(j=0;j<=i;j++)
			printf("%d ",matrix[i][j]);
		printf("\n");
	}
	printf("-----------\n");
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
			if(i<=j)
				printf("%d ",matrix[i][j]);
			else
				printf("  ");
		printf("\n");
	}
	return 0;
}
