#include<stdio.h>

int gcd1(int a,int b)
{
	return b>0?gcd1(b,a%b):a;
}

int gcd2(int a,int b)
{
	int temp;
	while(b)
	{
		temp=a%b;
		a=b;
		b=temp;
	}
	return a;
}

int lcm(int a,int b)
{
	return a*b/gcd2(a,b);
}

int main()
{
	int a,b;
	while(scanf("%d%d",&a,&b)!=EOF)
		printf("%d\n%d\n%d\n----------------\n",gcd1(a,b),gcd2(a,b),lcm(a,b));
	return 0;
}
