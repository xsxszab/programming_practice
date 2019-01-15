#include<stdio.h>

int main()
{
	int n;
	long ans;
	long temp;
	while(scanf("%d",&n)!=EOF)
	{
		ans=0;
		temp=2;
		while(n--)
		{
			ans+=temp;
			temp=temp*10+2;
		}
		printf("%ld\n",ans);
	}
	return 0;
}
