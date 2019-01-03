#include<stdio.h>

#define N 2

void print(int matrix[N][N])
{
	int i,j;
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
			printf("%d ",matrix[i][j]);
		printf("\n");
	}
}

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
	printf("---------------\n");
	print(matrix);
	return 0;
}
