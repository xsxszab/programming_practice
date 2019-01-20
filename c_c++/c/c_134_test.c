#include<stdio.h>

int add(int a,int b)
{
	return a+b;
}

int main()
{
	int m=2;
	int n=4;
	int ans;
	ans=add(m,n);
	printf("%d\n",ans);
	return 0;
}
