#include<stdio.h>
int main()
{
	long f1=1,f2=1;
	int n,i;
	scanf("%d",&n);
	if((n==1)|(n==2))
	{
		printf("1\n");
		return 0;
	}
	if(n>2)
	{
		long temp;
		for(i=2;i<n;i++)
		{
			temp=f1+f2;
			f1=f2;
			f2=temp;
		}
		printf("%ld",temp);
		return 0;
	}
	return -1;
}
