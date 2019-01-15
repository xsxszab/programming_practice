#include<stdio.h>

int add(int a,int b)
{
	return a+b;
}

int main()
{
	int a,b,ans;
	int (*p)(int,int);
	scanf("%d%d",&a,&b);
	p=add;
	ans=(*p)(a,b);
	printf("%d\n",ans);
	return 0;
}
