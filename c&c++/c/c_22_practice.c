#include<stdio.h>
#include<stdlib.h>

int main()
{
	int *person,i,node,m,n;
	scanf("%d%d",&m,&n);
	if(n==1)
	{
		for(i=1;i<m;i++)
			printf("%d is killed\n",i);
		printf("%d is the winner\n",m);
		return 0;
	}
	person=(int*)malloc(sizeof(int)*(m+1));
	for(i=1;i<m;i++)
		person[i]=i+1;
	person[m]=1;
	node=1;
	
	while(node!=person[node])
	{
		for(i=1;i<n-1;i++)
			node=person[node];
		printf("%d is killed\n",person[node]);
			person[node]=person[person[node]];
			node=person[node];
	}
	printf("%d is the winner\n",node);
	return 0;
}
