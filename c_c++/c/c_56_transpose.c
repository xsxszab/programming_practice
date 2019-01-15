#include<stdio.h>

#define N 4

int main()
{
	int i,j;
	int temp;
	int matrix[N][N];
	for(i=0;i<N;i++)
		for(j=0;j<N;j++)
			scanf("%d",&matrix[i][j]);
	printf("-------------\n");
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
			printf("%d ",matrix[i][j]);
		printf("\n");
	}
	printf("-------------\n");
	for(i=1;i<N;i++)
		for(j=0;j<i;j++)
			{
				temp=matrix[i][j];
				matrix[i][j]=matrix[j][i];
				matrix[j][i]=temp;
			}
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
			printf("%d ",matrix[i][j]);
		printf("\n");
	}
	printf("-------------\n");
	return 0;
}
