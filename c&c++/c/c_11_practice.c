#include<stdio.h>

int main()
{
	int n;
	while(scanf("%d",&n)!=0)
	{
		if((n<=0)||(n/1000!=0)||(n/10==0))
		{
			printf("error\n");
			continue;
		}
		int a,b,c;
		a=n/100;
		b=n/10%10;
		c=n%10;
		if(a*a*a+b*b*b+c*c*c==n)
			printf("yes\n");
		else
			printf("no\n");
	}
	return 0;
}
