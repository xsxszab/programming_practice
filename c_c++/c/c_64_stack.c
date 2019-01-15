#include<stdio.h>

#define N 4

int list[10]={0};
int len=0;


void print()
{
	int i;
	for(i=len-1;i>=0;i--)
		printf("%d ",list[i]);
	printf("\n");
}

int pop()
{
	return list[--len];
}

void push(int n)
{
	list[len++]=n;
}

int main()
{
	int i;
	int n;
	for(i=0;i<N;i++)
	{
		scanf("%d",&n);
		push(n);
	}
	printf("------------\n%d\n------------\n",pop());
	print();
	return 0;
}
