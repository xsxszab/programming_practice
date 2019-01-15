#include<stdio.h>

int pre[10]={0};

int search(int root)
{
	int i,temp;
	i=root;
	while(root!=pre[root])
		root=pre[root];
	while(i!=root)
	{
		temp=pre[i];
		pre[i]=root;
		i=temp;
	}
	return root;
}

void join(int root1,int root2)
{
	int x,y;
	x=search(root1);
	y=search(root2);
	if(x!=y)
	pre[y]=x;
}

int main()
{
	
	return 0;
}
