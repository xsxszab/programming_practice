#include<stdio.h>
#include<stdlib.h>

int main()
{
	int i;
	int len;
	int* list;
	scanf("%d",&len);
	list=(int*)malloc(len*sizeof(int));
	for(i=0;i<len;i++)
		scanf("%d",&list[i]);
	for(i=0;i<len;i++)
		printf("%d ",list[i]);
	printf("\n");
	free(list);
	return 0;
}
