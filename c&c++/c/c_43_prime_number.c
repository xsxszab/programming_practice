#include<stdio.h>
#include<math.h>

int main()
{
	int n;
	int i,temp,flag=1;
	while(scanf("%d",&n)!=EOF)
	{
		if(n==1)
		{
			printf("no\n");
			continue;
		}
		if(n==2)
		{
			printf("yes\n");
			continue;
		}
		temp=sqrt(n);
		for(i=2;i<temp;i++)
		{
			if(n%i==0)
			{
				flag=0;
				break;
			}
		}
		if(flag)
			printf("yes\n");
		else
			printf("no\n");
	}
	return 0;
}
