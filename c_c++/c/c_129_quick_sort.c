#include<stdio.h>

#define N 8

void swap(int *a,int *b)
{
	int temp;
	temp=*a;
	*a=*b;
	*b=temp;
}

void sort(int list[],int low,int high)
{
	if(low>=high)
		return;
	int i,j;
	int key=list[low];
	i=0;j=high;
	while(low<high)
	{
		while(low<high&&key<=list[high])
			high--;
		if(key>list[high])
			swap(&list[low++],&list[high]);
		while(low<high&&key>=list[low])
			low++;
		if(key<list[low])
			swap(&list[low],&list[high--]);
	}
	sort(list,i,low-1);
	sort(list,low+1,j);
}

int main()
{
	int i;
	int list[N];
	for(i=0;i<N;i++)
		scanf("%d",&list[i]);
	sort(list,0,N-1);
	for(i=0;i<N;i++)
		printf("%d ",list[i]);
	printf("\n");
	return 0;
}
