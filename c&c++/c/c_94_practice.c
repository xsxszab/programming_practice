#include<stdio.h>
#include<stdlib.h>

int main()
{
	int i,j;
	int row,col;
	int **matrix;
	scanf("%d%d",&row,&col);
	if((matrix=(int**)malloc(row*sizeof(int*)))==NULL)
	{
		printf("error\n");
		exit(1);
	}
	for(i=0;i<row;i++)
	{
		if((matrix[i]=(int*)malloc(col*sizeof(int)))==NULL)
		{
			printf("error\n");
			exit(1);
		}
	}
	for(i=0;i<row;i++)
		for(j=0;j<col;j++)
			scanf("%d",&matrix[i][j]);
	printf("-----------------------\n");
	for(i=0;i<row;i++)
	{
		for(j=0;j<col;j++)
			printf("%d ",matrix[i][j]);
		printf("\n");
	}
	printf("-----------------------\n");
	return 0;
}
