#include<stdio.h>

#define N 6

int main()
{
	int i,j;
	int matrix[N][N]={0};
	for(i=0;i<N;i++)
	{
		matrix[i][0]=1;
		matrix[i][i]=1;
	}
	for(i=1;i<N;i++)
		for(j=1;j<=i;j++)
		{
			matrix[i][j]=matrix[i-1][j-1]+matrix[i-1][j];
		}
	for(i=0;i<N;i++)
	{
		for(j=0;j<=i;j++)
				printf("%d ",matrix[i][j]);
		printf("\n");
	}
	return 0;
}
