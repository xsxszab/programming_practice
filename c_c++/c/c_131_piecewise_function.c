#include<stdio.h>

int func(int x)
{
	if(x<=1)
		return x;
	if(x>1&&x<10)
		return 2*x-1;
	return 3*x-11;
}

int main()
{
	int x,y;
	while(scanf("%d",&x)!=EOF)
	{
		y=func(x);
		printf("f(x)=%d\n------------\n",y);
	}
	return 0;
}
