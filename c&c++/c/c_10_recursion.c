#include<stdio.h>

int fibnacci(int n)
{	
	if((n==1)||(n==2))
		return 1;
	return fibnacci(n-1)+fibnacci(n-2);
}

int main()
{
	int n;
	long ans;
	while(scanf("%d",&n)!=0)
	{
		ans=fibnacci(n);
		printf("--------------\n");
		printf("%ld\n",ans);
		printf("--------------\n");
	}
	return 0;
}
