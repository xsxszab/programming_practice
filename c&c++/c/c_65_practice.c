#include<stdio.h>

#define N 4

void find_hole(int list[])
{
	int i=0;
	int flag=0;
	while((list[i]==0)&&(i<N))
		i++;
	if(i==N)
	{
		printf("no\n");
		return;
	}
	int sum=0;
	for(i=i+1;i<N;i++)
		sum+=list[i];
	if(sum)
		flag=1;
	if(flag)
		printf("yes\n");
	else
		printf("no\n");
}

int main()
{
	int i;
	int list[N]={0};
	for(i=0;i<N;i++)
		scanf("%d",&list[i]);
	find_hole(list);
	return 0;
}
