#include<stdio.h>

#define N 10
#define MAX 20

int main()
{
	int i,j;
	int list[N]={0};
	int storage[MAX]={0};
	for(i=0;i<N;i++)
		scanf("%d",&list[i]);
	for(i=0;i<N;i++)
	{
		printf("%d ",list[i]);
		if(list[i]>MAX)
		{
			printf("input error\n");
			return 1;
		}
	}
	printf("\n");
	for(i=0;i<N;i++)
		storage[list[i]]++;
	for(i=0;i<N;i++)
		if(storage[i])
		{
			for(j=0;j<storage[i];j++)
				printf("%d ",i);
		}
	printf("\n");
	return 0;
}
